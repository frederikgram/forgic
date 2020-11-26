""" """

import sys
import typing
import subprocess

sys.path.append("frontend")
sys.path.append("codegenerator")

from typing import * 

from frontend import lexer
from frontend import parser
from frontend.structs import Token, Construct

from codegenerator import generator
from codegenerator import regman
from codegenerator import prefabs

from utils import corree

def compile(inp: typing.IO, out: typing.IO, debug: bool = False):
    """ Runs the compilation process for .mcg files and writes .s files to disk """

    
    text = inp.read()
    if debug:
        print("# Original .mcg Source Code")
        print(text)

    # Convert a single-file input to a list of struct.Token(s)
    # describing the words (Tokens) type (Operator or Argument)
    tokens: List[Token] = lexer.lex(text)

    # Generate a list of struct.Construct(s) describing the actions
    # with the associated values that the tokens represent
    constructs: List[Construct] = parser.parse(tokens)

    if debug:
        print(f"# de-nested version of code found in {inp.name}")
        for con in constructs:
            toks = [con.operator]
            toks.extend(con.arguments)
            print(' '.join([tok.__str__() for tok in toks]))

    
    # Allocate real-machine registers to given variable names
    # and automatically stash values in the stack to allow for
    # more than 5 (the registers available to the user through this language)
    true_register_constructs: List[Construct] = regman.alloc(constructs)

    if debug:
        print(f"\n\n# Constructs with register names instead of variables")
        for con in true_register_constructs:
            toks = [con.operator]
            toks.extend(con.arguments)
            print(' '.join([tok.__str__() for tok in toks]))

    x86_instructions: List[str] = generator.generate(constructs)
    #optimized_instructions: List[str] = optimizer.optimize(x86_instructions)

    if debug:
        print(f"\n\n# Collection of prefabs")
        for val in x86_instructions:
            print(val)

    # Write initial boilerplate to output
    out.write(prefabs.boilerplate_start + "\n")

    # Write prefabs to output
    for instruction in x86_instructions:
        out.write(instruction + "\n")
    
    out.write(prefabs.boilerplate_end)


if __name__ == "__main__":

    xargs = {
        "input": str,
        "output": str,
        "debug": bool,
        "as": bool
    }

    success, args = corree.parse(' '.join(sys.argv), xargs)

    if not success:
        raise Exception("Unsuccessful argument parsing")
    
    inp = open(args["input"], 'r')
    out = open(args["output"], 'w')

    compile(inp, out, args["debug"])

    if args["as"] == True: 
        # assemble and link
        subprocess.run([f"as", "--gstabs", f"{out.name}", "-o", f"{out.name[:-1] + 'o'}"])
        subprocess.run([f"ld", f"{out.name[:-1] + 'o'}", "-o", f"{out.name[:-2]}"])
        

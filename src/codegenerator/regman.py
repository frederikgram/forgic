# Code for automatically handling register allocation and stack manipulation

import string

from typing import *
from structs import Construct, TokenType

from symboltable import symbol_table as stab
from symboltable import reset_table as rtab
from symboltable import registers

def _get_free_register() -> Union[int, None]:
    """ if a register that has no attached value, return it.
    otherwise, return None
    """

    free = [reg for reg in registers if reg not in stab.values()]
    
    if len(free) == 0:
        raise Exception("No free registers")
    else:
        return free[0]


def alloc(constructs: List[Construct]) -> List[Construct]:
    """ Convert naive-constructs to true-register constructs -
    a construct in which any Token whose tokentype is a variable
    has had its value converted from the argument name, to its
    corresponding register value (changes throughout the program)
    """

    for construct in constructs:
        for argument in construct.arguments:

            # Ignore token if it isnt a Variable
            if argument.tokentype != TokenType.VARIABLE:
                continue

            # If variable has a register representation,
            # set its value to the name of the register
            if argument.value in stab:
                argument.value = stab[argument.value]

            # Otherwise, find a free register and 
            # assign the arguments value to it
            else:
                stab[argument.value] = _get_free_register()
                argument.value = stab[argument.value]
       

    return constructs


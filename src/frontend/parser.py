""" """

import string
from typing import *
from structs import Token, TokenType, Construct
from grammar import operator_table, ActionDescriptor



def parse(token_lines: List[List[Token]]) -> List[Construct]:
    """ Creates a list of Constructs from a given list of Tokens
    during parsing, the source-code will also be type-checked """


    def _parse_operator(operator: Token, tokens: List[Token]) -> List[Construct]:
        """ Recursively parses operators found in a list of tokens, and converts them
        into a list of Constructs
        """
        
        # Fetch ActionDescriptor for given operator
        if operator.value not in operator_table:
            raise Exception(f"Supposed Operator was not found in the operator table: '{operator.value}'")
        
        descriptor = operator_table[operator.value]
        argument_buffer: List[Token] = list()
        constructs: List[Construct] = list()
        deep_constructs: List[Construct] = list()

        # Parse
        while len(tokens) > 0:
            token = tokens.pop(0)

            # Nested Calculation
            if token.tokentype == TokenType.OPERATOR:
                if len(argument_buffer) != descriptor.n_args:

                    # Add calculation buffer as arg
                    argument_buffer.append(
                        Token("buf", TokenType.ARGUMENT)
                    )

                # Recursively Parse the nested Action
                deep_constructs = _parse_operator(token, tokens)
            else:
                argument_buffer.append(token)

        constructs.extend(deep_constructs)
        constructs.append(
            Construct(operator, argument_buffer)
        )

        return constructs

    def _parse_line(line: List[Token]) -> List[Construct]:
        """ Takes in a list of tokens, representing the tokens found in a
        single newline-delimited sequence of words from an input file
        """

        operator = line.pop(0)
        
        if operator.tokentype != TokenType.OPERATOR:
            raise Exception(f"Expected operator, found argument: {operator.value}")

        return _parse_operator(operator, line)
    
   
    constructs = list()
    for line in token_lines:
        constructs.extend(_parse_line(line))

    return constructs
   

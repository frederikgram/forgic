""" Generates a List of Tokens from a given input string """
from typing import *
from structs import Token, TokenType
from grammar import operator_table

def _get_token_type(word: str) -> TokenType:
    """ Naive approach to classifying token types """
   
    if word in operator_table:
        return TokenType.OPERATOR
    elif word.isdigit():
        return TokenType.LITERAL
    else:
        return TokenType.VARIABLE

def lex(text: str) -> List[Token]:
    """ Convert a block of text to a list of structs.Token(s) """

    token_lines: List[Token] = list()

    for line in text.splitlines():
        token_line = list()

        # Ignore blank lines
        if line.isspace() or line == "":
            continue

        # Ignore Comments lines
        if line.startswith('/'):
            continue

        for word in line.split():
            token_line.append(Token(value = word, tokentype = _get_token_type(word)))
        
        token_lines.append(token_line)

    return token_lines


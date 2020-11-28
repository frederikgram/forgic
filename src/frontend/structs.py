""" """

from typing import *
from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    OPERATOR = 1
    LITERAL = 2
    VARIABLE = 3

@dataclass
class Token:
    value: str
    tokentype: TokenType

    def __str__(self) -> str:
        return self.value

@dataclass
class Construct:
    operator: Token
    arguments: List[Union[Token, "Construct"]]

 

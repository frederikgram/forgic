""" """

from typing import *
from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    OPERATOR = 1
    ARGUMENT = 2

@dataclass
class Token:
    value: str
    tokentype: TokenType

    def __str__(self) -> str:
        return self.value

@dataclass
class Construct:
    operator: Token

    # @Future / Allow for arguments of type "Construct", which in turn allows for both parse- and as-trees
    arguments: List[Union[Token, "Construct"]]

 

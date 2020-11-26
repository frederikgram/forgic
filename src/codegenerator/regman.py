# Code for automatically handling register allocation and stack manipulation

import string

from typing import *
from structs import Construct

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
    """ Convert naive-constructs to true-register constructs """


    i = 0
    while i < len(constructs):
        construct = constructs[i]

        # iterate over single construct args
        for argument in construct.arguments:

            if argument.value in stab:
                argument.value = stab[argument.value]

            elif argument.value[0] in string.ascii_letters:
                
                stab[argument.value] = _get_free_register()
                argument.value = stab[argument.value]
       
        i += 1

    return constructs


""" """

import prefabs

from typing import * 
from frontend.structs import Construct
from symboltable import symbol_table as stab


def _find_prefab_for_construct(construct: Construct) -> List[str]: 
    
    opval = construct.operator.value

    if opval == "assign":

        # Assign a literal
        if construct.arguments[1].value.startswith('r') == False: 
            prefab = prefabs.move_literal_to_register

            register = construct.arguments[0].value
            literal = construct.arguments[1].value
            
            prefab = prefab.format(literal, register)
            return [prefab]
    
        else:
            prefab = prefabs.move_register_to_register
            
            to_reg = construct.arguments[0].value
            from_reg = construct.arguments[1].value

            prefab = prefab.format(from_reg, to_reg)
            return [prefab]

    if opval == "add":

        # Add a literal
        if construct.arguments[1].value.startswith('r') == False: 

            # Add a literal and a literal
            if construct.arguments[0].value.startswith('r') == False:
                pass

            # Add a literal and a register
            else:
                prefab = prefabs.add_literal_to_register

                literal = construct.arguments[1].value
                to_reg = construct.arguments[0].value
        
                prefab = prefab.format(literal = literal, to_reg = to_reg)
                return [prefab]
             
        # Add a register and a register
        else:
        
            prefab = prefabs.add_register_to_register

            reg1 = construct.arguments[0].value
            reg2 = construct.arguments[1].value

            prefab = prefab.format(reg1 = reg1, reg2 = reg2)
            return  [prefab]

    if opval == "write":

        # Write Register Value
        if construct.arguments[0].value.startswith('r') == True:
            prefab = prefabs.write_register_to_stdout

            register = construct.arguments[0].value

            prefab = prefab.format(reg = register)
            return [prefab]

    return [None]

def generate(constructs: List[Construct]) -> List[str]:


    out = list()

    for construct in constructs:

        prefab = _find_prefab_for_construct(construct)
        if prefab == [None]:
            out.extend([str(construct)])
        else:
            out.extend(prefab)    

    return out


""" Symbol Table for Automatic Register, variable and Stack Management """

from typing import *


registers = ["r10", "r11", "r12", "r13", "r14", "r15"]

symbol_table: Dict[str, str] = dict()

# Set name-register pair of "buf, r9" to be the builtin standard
# output buffer for any calculation action in the language

symbol_table["buf"] = "r9"


reset_table: Dict[str, str] = dict()

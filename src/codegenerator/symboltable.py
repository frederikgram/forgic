""" Symbol Table for Automatic Register, variable and Stack Management """

from typing import *

# Register r8 and r9 are used internally for respectively a
# temporary variable buffer and an output buffer for calculations
registers = ["r10", "r11", "r12", "r13", "r14", "r15"]
symbol_table: Dict[str, str] = dict()

# Every key, value (variable, register) in this table
# is reset after every action, and allows
# for switching variables to different registers
reset_table: Dict[str, str] = dict()

# Internal Variable names
temporary_variable_buffer_variable_name = "__variable_buffer"
calculation_buffer_variable_name = "__calculation_buffer"

# Set Internal Variable Names in Symbol table
symbol_table[temporary_variable_buffer_variable_name] = "r8"
symbol_table[calculation_buffer_variable_name] = "r9"


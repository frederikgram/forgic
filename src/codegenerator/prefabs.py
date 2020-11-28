""" """

from typing import *
from symboltable import symbol_table as stab
from symboltable import temporary_variable_buffer_variable_name

vb_reg = stab[temporary_variable_buffer_variable_name]

move_literal_to_register = "movq ${}, %{}"
move_register_to_register = "movq %{}, %{}"

add_literal_to_register = """movq %{to_reg}, %r8 
addq ${literal}, %{to_reg}
movq %{to_reg}, %r9
movq %r8, %{to_reg}"""

add_register_to_register = """movq %{reg2}, %r8 
addq %{reg1}, %{reg2}
movq %{reg2}, %r9
movq %r8, %{reg2}"""

add_literal_to_literal = """movq ${lit1}, %r9
addq ${lit2}, %r9"""

write_register_to_stdout = """# Write {reg} to stdout
movq $1, %rax
movq $1, %rdi
movq %{reg}, %rsi
movq $1, %rdx
syscall"""


boilerplate_start = """.section .data
.section .text
.globl _start
_start:"""


boilerplate_end = """#Syscall exit program
movq $60, %rax
movq $0, %rdi
syscall
"""

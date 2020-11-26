.section .data
.section .text
.globl _start
_start:
movq $1, %r10
movq $2, %r11
movq $0, %r12
movq %r11, %r8 
addq %r10, %r11
movq %r11, %r9
movq %r8, %r11
movq %r9, %r12
# Write r12 to stdout
movq $1, %rax
movq $1, %rdi
movq %r12, %rsi
movq $1, %rdx
syscall
#Syscall exit program
movq $60, %rax
movq $0, %rdi
syscall

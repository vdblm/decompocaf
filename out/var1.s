.data # Data section
x_1: .word 0

newLINE: .asciiz "\n" 
.text
main:
li $s0, 2
move $t0, $s0
sw $t0, x_1

lw $t0, x_1
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

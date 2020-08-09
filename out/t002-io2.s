.data # Data section
a_1: .word 0
b_1: .word 0
i_1: .word 0

newLINE: .asciiz "\n" 
.text
main:
li $s0, 0
move $t0, $s0
sw $t0, b_1

FOOR_START_0:
li $s0, 1

beq $s0, $0, FOOR_END_0
sll $0, $0, 0
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 1

move $s2, $s0 
add $s0, $s1 $s2
move $t0, $s0
sw $t0, i_1

j FOOR_START_0
FOOR_END_0: sll $0, $0, 0

lw $t0, i_1
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
lw $t0, b_1
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

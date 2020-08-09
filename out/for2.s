.data # Data section
i_1: .word 0

newLINE: .asciiz "\n" 
.text
main:
FOOR_START_0:
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 0

move $s2, $s0 
slt $s0, $s2 $s1

beq $s0, $0, FOOR_END_0
sll $0, $0, 0
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 2

move $s2, $s0 
sub $s0, $s1 $s2
move $t0, $s0
sw $t0, i_1

j FOOR_START_0
FOOR_END_0: sll $0, $0, 0

li $v0, 4
la $a0, newLINE
syscall #print new line

lw $t0, i_1
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

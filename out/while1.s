.data # Data section
i_1: .word 0

newLINE: .asciiz "\n" 
.text
main:
li $s0, 0
move $t0, $s0
sw $t0, i_1

WHILLE_START_0:
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 5

move $s2, $s0 
slt $s0, $s1 $s2

beq $s0, $0, WHILLE_END_0
sll $0, $0, 0
lw $t0, i_1
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 1

move $s2, $s0 
add $s0, $s1 $s2
move $t0, $s0
sw $t0, i_1

j WHILLE_START_0
WHILLE_END_0: sll $0, $0, 0
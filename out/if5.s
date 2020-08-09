.data # Data section
i_1: .word 0

newLINE: .asciiz "\n" 
.text
main:
li $s0, 0
move $t0, $s0
sw $t0, i_1

lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 12

move $s1, $s0 
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 12

move $s1, $s0 
li $s0, 3

move $s1, $s0 
li $s0, 5

move $s1, $s0 
li $s0, 1

move $s2, $s0 
and $s0, $s1 $s2

move $s2, $s0 
seq $s0, $s1 $s2

move $s2, $s0 
or $s0, $s1 $s2

move $s2, $s0 
slt $s0, $s1 $s2

move $s2, $s0 
or $s0, $s1 $s2

move $s2, $s0 
slt $s0, $s2 $s1

beq $s0, $0, IIF_10
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_20
IIF_10: sll $0, $0, 0
IIF_20: sll $0, $0, 0

li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

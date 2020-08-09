.data # Data section
a_1: .word 0
b_2: .word 0
i_2: .word 0

newLINE: .asciiz "
" 
.text

main:
li $s0, 2
move $t0, $s0
sw $t0, a_1

lw $t0, a_1
move $s0, $t0

li $s0, 2

move $s2, $s1 
move $s1, $s0 
sle $s0, $s1 $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

lw $t0, a_1
move $s0, $t0

li $s0, 2

move $s2, $s1 
move $s1, $s0 
sle $s0, $s1 $s2

beq $s0, $0, IIF_0
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 3
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 4
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 5
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 6
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_0: sll $0, $0, 0

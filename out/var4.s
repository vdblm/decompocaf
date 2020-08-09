.data # Data section
a_1: .word 0
b_2: .word 0
a_3: .word 0
b_4: .word 0
c_5: .word 0
d_5: .byte 0

newLINE: .asciiz "\n" 
.text


main:
li $s0, 10
move $t0, $s0
sw $t0, a_3

li $s0, 82
move $t0, $s0
sw $t0, b_2

li $s0, 5
move $t0, $s0
sw $t0, b_4

lw $t0, b_4
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 12
move $t0, $s0
sw $t0, c_5

lw $t0, c_5
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

lw $t0, a_3
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
lw $t0, b_2
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

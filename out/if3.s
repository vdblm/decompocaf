.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $s0, 1

beq $s0, $0, IIF_10
sll $0, $0, 0
li $s0, 0

beq $s0, $0, IIF_11
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_21
IIF_11: sll $0, $0, 0
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_21: sll $0, $0, 0

j IIF_20
IIF_10: sll $0, $0, 0
li $s0, 3
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_20: sll $0, $0, 0

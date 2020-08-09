.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $v0, 4
la $a0, newLINE
syscall #print new line

li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $v0, 5
syscall # read integer
move $s0, $v0

beq $s0, $0, IIF_10
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_20
IIF_10: sll $0, $0, 0
IIF_20: sll $0, $0, 0

li $v0, 5
syscall # read integer
move $s0, $v0

beq $s0, $0, IIF_11
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_21
IIF_11: sll $0, $0, 0
IIF_21: sll $0, $0, 0

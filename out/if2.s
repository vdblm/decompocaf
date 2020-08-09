.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $s0, 1

move $s1, $s0 
li $s0, 1

move $s2, $s0 
seq $s0, $s1 $s2

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
li $s0, 2

move $s1, $s0 
li $s0, 1

move $s2, $s0 
seq $s0, $s1 $s2

beq $s0, $0, IIF_11
sll $0, $0, 0
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_21
IIF_11: sll $0, $0, 0
li $s0, 3
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_21: sll $0, $0, 0

IIF_20: sll $0, $0, 0

li $s0, 1

move $s1, $s0 
li $s0, 2

move $s2, $s0 
seq $s0, $s1 $s2

beq $s0, $0, IIF_12
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_22
IIF_12: sll $0, $0, 0
li $s0, 2

move $s1, $s0 
li $s0, 2

move $s2, $s0 
seq $s0, $s1 $s2

beq $s0, $0, IIF_13
sll $0, $0, 0
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_23
IIF_13: sll $0, $0, 0
li $s0, 3
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_23: sll $0, $0, 0

IIF_22: sll $0, $0, 0

li $s0, 1

move $s1, $s0 
li $s0, 2

move $s2, $s0 
seq $s0, $s1 $s2

beq $s0, $0, IIF_14
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_24
IIF_14: sll $0, $0, 0
li $s0, 2

move $s1, $s0 
li $s0, 1

move $s2, $s0 
seq $s0, $s1 $s2

beq $s0, $0, IIF_15
sll $0, $0, 0
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_25
IIF_15: sll $0, $0, 0
li $s0, 3
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_25: sll $0, $0, 0

IIF_24: sll $0, $0, 0

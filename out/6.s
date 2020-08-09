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
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_21: sll $0, $0, 0

li $v0, 5
syscall # read integer
move $s0, $v0

beq $s0, $0, IIF_12
sll $0, $0, 0
li $s0, 0

beq $s0, $0, IIF_13
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_23
IIF_13: sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_23: sll $0, $0, 0

li $s0, 1

beq $s0, $0, IIF_14
sll $0, $0, 0
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_24
IIF_14: sll $0, $0, 0
IIF_24: sll $0, $0, 0

li $s0, 1

beq $s0, $0, IIF_15
sll $0, $0, 0
li $s0, 3
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 0

beq $s0, $0, IIF_16
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_26
IIF_16: sll $0, $0, 0
li $s0, 4
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 0

beq $s0, $0, IIF_17
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_27
IIF_17: sll $0, $0, 0
li $s0, 5
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $v0, 5
syscall # read integer
move $s0, $v0

beq $s0, $0, IIF_18
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_28
IIF_18: sll $0, $0, 0
li $s0, 0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_28: sll $0, $0, 0

IIF_27: sll $0, $0, 0

IIF_26: sll $0, $0, 0

j IIF_25
IIF_15: sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_25: sll $0, $0, 0

j IIF_22
IIF_12: sll $0, $0, 0
li $s0, 0

beq $s0, $0, IIF_19
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_29
IIF_19: sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

IIF_29: sll $0, $0, 0

li $s0, 1

beq $s0, $0, IIF_110
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j IIF_210
IIF_110: sll $0, $0, 0
IIF_210: sll $0, $0, 0

IIF_22: sll $0, $0, 0

.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $s0, 1

move $s1, $s0 
li $s0, 1

move $s2, $s0 
add $s0, $s1, $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 10

move $s1, $s0 
li $s0, 5

move $s2, $s0 
sub $s0, $s1, $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 21

move $s1, $s0 
li $s0, 3

div $s1, $s0 
mflo $s0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 345

move $s1, $s0 
li $s0, 56

move $s2, $s0 
mul $s0, $s1, $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 82

move $s1, $s0 
li $s0, 9

div $s1, $s0 
mfhi $s0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

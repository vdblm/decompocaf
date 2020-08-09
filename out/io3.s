.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $s0, 4
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 4

move $s1, $s0 
li $s0, 8

move $s1, $s0 
li $s0, 1

move $s2, $s0 
add $s0, $s1 $s2

move $s2, $s0 
mul $s0, $s1, $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $s0, 8

move $s1, $s0 
li $s0, 3

move $s1, $s0 
li $s0, 2

move $s2, $s0 
sub $s0, $s1 $s2

move $s2, $s0 
sub $s0, $s1 $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

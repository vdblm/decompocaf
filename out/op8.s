.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $s0, 0

move $s1, $s0 
li $s0, 1

move $s2, $s0 
sge $s0, $s1 $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 0

move $s1, $s0 
li $s0, 0

move $s2, $s0 
sge $s0, $s1 $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li $s0, 1

move $s1, $s0 
li $s0, 0

move $s2, $s0 
sge $s0, $s1 $s2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

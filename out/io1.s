.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $v0, 5
syscall # read integer
move $s0, $v0

li $v0, 4
la $a0, newLINE
syscall #print new line

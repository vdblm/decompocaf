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

.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line
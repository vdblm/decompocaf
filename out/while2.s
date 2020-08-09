.data # Data section

newLINE: .asciiz "\n" 
.text
main:
WHILLE_START_0:
li $s0, 1

beq $s0, $0, WHILLE_END_0
sll $0, $0, 0
li $s0, 1
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j WHILLE_END_0
li $s0, 2
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

j WHILLE_START_0
WHILLE_END_0: sll $0, $0, 0

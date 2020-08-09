.data # Data section

newLINE: .asciiz "\n" 
.text
main:
WHILLE_START_0:
li $v0, 5
syscall # read integer
move $s0, $v0

beq $s0, $0, WHILLE_END_0
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j WHILLE_START_0
WHILLE_END_0: sll $0, $0, 0

WHILLE_START_1:
li $v0, 5
syscall # read integer
move $s0, $v0

beq $s0, $0, WHILLE_END_1
sll $0, $0, 0
li $v0, 4
la $a0, newLINE
syscall #print new line

j WHILLE_START_1
WHILLE_END_1: sll $0, $0, 0

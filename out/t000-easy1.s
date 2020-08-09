.data # Data section
i_1: .float 0.0

newLINE: .asciiz "\n" 
.text
main:
<<<<<<< HEAD
li $s0, 0
move $t0, $s0
sw $t0, b_1

li $s0, 1
move $t0, $s0
sw $t0, i_1

FOOR_START_0:
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 5

move $s2, $s0 
slt $s0, $s1, $s2

beq $s0, $0, FOOR_END_0
sll $0, $0, 0
lw $t0, i_1
move $s0, $t0

move $s1, $s0 
li $s0, 1

move $s2, $s0 
add $s0, $s1, $s2
move $t0, $s0
sw $t0, i_1

j FOOR_START_0
FOOR_END_0: sll $0, $0, 0

lw $t0, b_1
move $s0, $t0
move $a0, $s0
li $v0, 1
=======
li.d $f0, 5.5
mov.d $f5, $f0
s.s $f5, i_1

l.s $f5, i_1
mov.d $f0, $f5
mov.d $f12, $f0
li $v0, 2
>>>>>>> f9a5243c06a19211c27590e0fef23d8198c62fd4
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

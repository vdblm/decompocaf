.data # Data section
a_1: .word 0
b_1: .word 0
c_1: .word 0
d_1: .word 0
z_1: .word 0

newLINE: .asciiz "
" 
.text
main:
li $v0, 5
syscall # read integer
move $s0, $v0
move $t0, $s0
sw $t0, a_1

li $v0, 5
syscall # read integer
move $s0, $v0
move $t0, $s0
sw $t0, b_1

li $v0, 5
syscall # read integer
move $s0, $v0
move $t0, $s0
sw $t0, c_1

li $v0, 5
syscall # read integer
move $s0, $v0
move $t0, $s0
sw $t0, d_1

lw $t0, a_1
move $s0, $t0

lw $t0, b_1
move $s0, $t0

lw $t0, c_1
move $s0, $t0

lw $t0, d_1
move $s0, $t0

lw $t0, a_1
move $s0, $t0

move $s2, $s0 
div $s0, $s1 
mflo $s0

move $s2, $s1 
move $s1, $s0 
sub $s0, $s1 $s2

move $s2, $s1 
move $s1, $s0 
muhi $s0

move $s2, $s1 
move $s1, $s0 
add $s0, $s1 $s2
move $t0, $s0
sw $t0, z_1

lw $t0, z_1
move $s0, $t0
move $a0, $s0
li $v0, 1
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line
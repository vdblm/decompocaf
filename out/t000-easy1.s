.data # Data section
i_1: .float 0.0

newLINE: .asciiz "\n" 
.text
main:
li.d $f0, 5.5
mov.d $f5, $f0
s.s $f5, i_1

l.s $f5, i_1
mov.d $f0, $f5
mov.d $f12, $f0
li $v0, 2
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

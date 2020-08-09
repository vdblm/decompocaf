.data # Data section

newLINE: .asciiz "\n" 
.text
main:
li.d $f0, 3.1415
mov.d $f12, $f0
li $v0, 2
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li.d $f0, 3.14159265
mov.d $f12, $f0
li $v0, 2
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

li.d $f0, 575450595.1415
mov.d $f12, $f0
li $v0, 2
syscall    # print!
li $v0, 4
la $a0, newLINE
syscall #print new line

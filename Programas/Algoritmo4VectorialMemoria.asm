addi $0, $0, 0  //relleno
addi $t0, $0, 8
addi $t0, $0, 8
addi $s0, $0, 6
addi $s1, $0, 30
sb $s0, 0($s1)
addi $s0, $0, 215
sb $s0, 1($s1)
addi $s0, $0, 120
sb $s0, 2($s1)
addi $s0, $0, 70
sb $s0, 3($s1)
vlbu $s0, 0($s1)  
addi $t2, $0, 0
encriptacion1:
vlbu $t3, 0($t2) //encriptacion1
vadd $t4, $t3, $s0
add $t5, $t2, $t0
vsb $t4, 0($t5)
addi $t2, $t2, 4
slt $t6, $t2, $t0
bne $t6, $0, encriptacion1
add $t7, $t0, $t0
desencriptacion1:
vlbu $t3, 0($t2)  //desencriptacion1
vsub $t4, $t3, $s0
add $t5, $t2, $t0
vsb $t4, 0($t5)
addi $t2, $t2, 4
slt $t6, $t2, $t7
bne $t6, $0, desencriptacion1 
while1: 
j while1
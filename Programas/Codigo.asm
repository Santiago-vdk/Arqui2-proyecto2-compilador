addi $0, $0, (3)
addi $1, $1, (3)
movi $11, (18)
lb $11, $11
movi $12, (0)
lb $12, $12
movi $13, (9)
lb $13, $13
for1:
beq $7, $0, end
for2:
movi $16, (70)
beq $8, $1, endFor2
for3:
movi $17, (71)
addi $5, $7, (3)
beq $9, $5, endFor3
for4:
movi $18, (72)
addi $5, $8, (3)
beq $10, $5, endFor4
if:
movi $19, (73)
beq $9, $14, ifFalse
beq $10, $14, ifFalse
addi $5, $0, (1)
beq $9, $5, ifFalse
addi $5, $1, (1)
beq $10, $5, ifFalse
subi $5, $9, (1)
mult $5, $1, $5
subi $6, $10, 1
add $5, $5, $6
add $5, $5, $13
lb $5, $5
add $6, $6, $12
lb $6, $6
mult $5, $5, $6
add $3, $3, $5
ifFalse:
movi $20, (74)
addi $2, $2, (1)
addi $10, $10, (1)
j for4
endFor2:
movi $21, (75)
movi $8, (0)
addi $7, $7, (1)
j for1
endFor3:
movi $22, (76)
mov $9, $7
movi $2, (0)
add $4, $4, $11
sb $3, $4
addi $4, $4, (1)
mov $3, $14
addi $8, $8, (1)
mov $10, $8
j for2
endFor4:
movi $23, (77)
addi $9, $9, (1)
mov $10, $8
j for3
end:
movi $0, (18)
lb $10, $0
addi $0, $0, (1)
lb $11, $0
addi $0, $0, (1)
lb $12, $0
addi $0, $0, (1)
lb $13, $0
addi $0, $0, (1)
lb $14, $0
addi $0, $0, (1)
lb $15, $0
addi $0, $0, (1)
lb $16, $0
addi $0, $0, (1)
lb $17, $0
addi $0, $0, (1)
lb $18, $0
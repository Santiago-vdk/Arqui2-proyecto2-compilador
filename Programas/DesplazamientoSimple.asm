ADDI $t0, $0, 100   //guardo en t0 la cantidad de pixeles
ADDI $t2, $0, 0      //inicializando el indice en 1
encriptacion2:
LB $t3, 0($t2)         // $t3 es Dato y se carga lo que está en indice
SLL $t4, $t3, 2   //Resultado es $t4
ADD $t5, $t2, $t0   // $t5 es nuevadireccion
SB $t4, 0($t5)        //guardamos el resultado del shift en memoria
ADDI $t2, $t2, 1      //Indice++
SLT $t6, $t2, $t0     //Si el indice es menor a la cantidad de pixeles, t6 es 1
BNE $t6, $0, encriptacion2   //si es diferente de 0 entonces repite el ciclo
ADD $t7, $t0, $t0   //obtenemos doblepixeles
desencriptacion2: 
LB $t3, 0($t2)         // $t3 es Dato y se carga lo que está en indice
SRL $t4, $t3, 2   //Resultado es $t4
ADD $t5, $t2, $t0   // $t5 es nuevadireccion
SB $t4, 0($t5)        //guardamos el resultado del shift en memoria
ADDI $t2, $t2, 1      //Indice++
SLT $t6, $t2, $t7     //Si el indice es menor al doble de pixeles		
BNE $t6, $0, desencriptacion2  //si es diferente de 0 entonces repite el ciclo
while1:
j while1 //ciclo infinito
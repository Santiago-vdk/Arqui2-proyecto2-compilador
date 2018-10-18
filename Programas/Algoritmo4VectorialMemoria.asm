		addi $t0, $0, 8     //guardo en t0 la cantidad de pixeles
		addi $t1, $0, 6     //guardamos en t1 la clave a usar
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacions1:
		lbu $t3, 0($t2)           // $test? en indice
		xor $t4, $t3, $t1     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //gor en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t0       //Si s te el ciclo
		bne $t6, $0, encriptacions1     //si es diferente
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacions1: 
		lbu $t3, 0($t2)           // $targa lo que est? en indice
		xor $t4, $t3, $t1     //Resultado es $t4
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		sb $t4, 0($t5)          //guesultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el menor al doble de pixeles		
		bne $t6, $0, desencriptacions1    //si ente de 0 entonces repite
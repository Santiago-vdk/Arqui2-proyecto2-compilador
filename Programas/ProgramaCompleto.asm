		addi $t0, $0, 5     //guardo en t0 la cantidad de pixeles
		addi $t1, $0, 6     //guardamos en t1 la clave a usar
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacions1:
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		xor $t4, $t3, $t1     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacions1     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacions1: 
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		xor $t4, $t3, $t1     //Resultado es $t4
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacions1    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $t0, $0, 5     //guardo en t0 la cantidad de pixeles
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacions2:
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		sll $t4, $t3, 3     //Resultado es $t4
	    add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del shift en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacions2     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacions2: 
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		srl $t4, $t3, 3     //Resultado es $t4
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del shift en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacions2    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $t0, $0, 5     //guardo en t0 la cantidad de pixeles
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacions3:
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		sll $t1, $t3, 3     //rotate left block
		srl $t4, $t3, 5     //8-3
		or $t4, $t1, $t4    //OR para obtener la rotacion
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del rotate en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacions3     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacions3: 
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		srl $t1, $t3, 3 
		sll $t4, $t3, 5     //8-3
		or $t4, $t1, $t4    //OR para obtener la rotacion
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del rotate en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacions3    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $0, $0, 0    //instruccion vacia
		addi $t0, $0, 8     //guardo en t0 la cantidad de pixeles
		addi $s0, $0, 6     //guardamos en t1 la primera constante
		addi $s1, $0, 215     //guardamos en t1 la primera constante
		addi $s2, $0, 120     //guardamos en t1 la primera constante
		addi $s3, $0, 70     //guardamos en t1 la primera constante
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacions4:
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		add $t4, $t3, $s0     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado de la suma en memoria
		addi $t2, $t2, 1        //Indice++
		
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		add $t4, $t3, $s1     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado de la suma en memoria
		addi $t2, $t2, 1        //Indice++
		
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		add $t4, $t3, $s2     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado de la suma en memoria
		addi $t2, $t2, 1        //Indice++
		
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		add $t4, $t3, $s3     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado de la suma en memoria
		addi $t2, $t2, 1        //Indice++
		
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacions4     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacions4: 
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		sub $t4, $t3, $s0     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		sub $t4, $t3, $s1     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		sub $t4, $t3, $s2     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		
		lbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		sub $t4, $t3, $s3     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		sb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacions4    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $t0, $0, 8     //guardo en t0 la cantidad de pixeles
		vaddi $t1, $0, 6     //guardamos en t1 la clave a usar
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacionp1:
		vlbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		vxor $t4, $t3, $t1     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 4        //Indice+=4
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacionp1     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacionp1: 
		vlbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		vxor $t4, $t3, $t1     //Resultado es $t4
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado del xor en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacionp1    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $t0, $0, 8     //guardo en t0 la cantidad de pixeles
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacionp2:
		vlbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		vsll $t4, $t3, 3     //Resultado es $t4
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado del shift en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacionp2     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacionp2: 
		vlbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		vsrl $t4, $t3, 3     //Resultado es $t4
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado del shift en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacionp2    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $t0, $0, 8     //guardo en t0 la cantidad de pixeles
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacionp3:
		vlbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		vrotl $t4, $t3, 3     //rotate left
		add $t5, $t2, $t0     // $t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado del rotate en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacionp3     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacionp3: 
		vlbu $t3, 0($t2)           // $t3 es Dato y se carga lo que est? en indice
		vrotr $t4, $t3, 3     //rotate right
		add $t5, $t2, $t0     //   $t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado del rotate en memoria
		addi $t2, $t2, 1        //Indice++
		slt $t6, $t2, $t7       //Si el indice es menor al doble de pixeles		
		bne $t6, $0, desencriptacionp3    //si es diferente de 0 entonces repite el ciclo
		j while1
		addi $0, $0, 0    //instruccion de relleno
		addi $t0, $0, 8     //guardo en t0 la cantidad de pixeles
		addi $s0, $0, 6     //guardamos en t1 la primera constante
		addi $s1, $0, 31000   //guardamos la direccion a la que quiero guardar el vector de suma
		sb $s0, 0($s1)   //se guarda en memoria la primera contante
		addi $s0, $0, 215     //cargamos la siguiente constante
		sb $s0, 1($s1)   //se guarda en memoria la siguiente contante
		addi $s0, $0, 120     //cargamos la siguiente constante
		sb $s0, 2($s1)   //se guarda en memoria la siguiente contante
		addi $s0, $0, 70     //cargamos la siguiente constante
		sb $s0, 3($s1)   //se guarda en memoria la siguiente contante
		vlbu $s0, 0($s1)   //obtenemos el vector de suma
		addi $t2, $0, 0        //inicializando el indice en 0
encriptacionp4:
		vlbu $t3, 0($t2)           // $t3 es el vector que esta en la direccion del indice
		vadd $t4, $t3, $s0     //suma vectorial y se guarda en $t4
		add $t5, $t2, $t0     //$t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado de la suma en memoria
		addi $t2, $t2, 4        //Indice+=4
		slt $t6, $t2, $t0       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, encriptacionp4     //si es diferente de 0 entonces repite el ciclo
		add $t7, $t0, $t0     //obtenemos doblepixeles
desencriptacionp4: 
		vlbu $t3, 0($t2)           // $t3 es el vector que esta en la direccion del indice
		vsub $t4, $t3, $s0     //resta vectorial y se guarda en $t4
		add $t5, $t2, $t0     //$t5 es nuevadireccion
		vsb $t4, 0($t5)          //guardamos el resultado de la suma en memoria
		addi $t2, $t2, 4        //Indice+=4
		slt $t6, $t2, $t7       //Si el indice es menor a la cantidad de pixeles, t6 es 1
		bne $t6, $0, desencriptacionp4     //si es diferente de 0 entonces repite el ciclo
		j while1
while1:
		j while1

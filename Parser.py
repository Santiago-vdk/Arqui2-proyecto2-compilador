from Instrucciones import *


def extraerOperandos(line, i):
    line = line.split()

    # Reemplazo de cada linea las ','
    k = 0
    while k < len(line):
        line[k] = line[k].replace(",", "")
        k += 1

    # Averiguo el tipo de instruccion para extraer sus operandos
    instruccion = line[0]
    if(instruccion in instrucciones_r):
        registroA = line[1]
        registroB = line[2]
        registroC = line[3]
        tupla = [i, instruccion, registroA, registroB, registroC]
        return tupla

    elif(instruccion in instrucciones_r_2Operandos):
        registroA = line[1]
        registroB = line[2]
        tupla = [i, instruccion, registroA, registroB]
        return tupla

    elif(instruccion in instrucciones_i):
        registroA = line[1]
        registroB = line[2]
        inmediato = line[3]
        inmediato = inmediato.replace("(", "")
        inmediato = inmediato.replace(")", "")
        tupla = [i, instruccion, registroA, registroB, inmediato]
        return tupla

    elif(instruccion in instrucciones_i_2Operandos):
        registroA = line[1]
        inmediato = line[2]
        inmediato = inmediato.replace("(", "")
        inmediato = inmediato.replace(")", "")
        tupla = [i, instruccion, registroA, inmediato]
        return tupla

    elif(instruccion in instrucciones_j):
        label = line[1]
        tupla = [i, instruccion, label]
        return tupla

    else:
        label = instruccion
        label = label.replace(":", "")
        tupla = [i, label]
        return tupla


def encontrarEtiqueta(instrucciones, etiqueta):
    for instruccion in instrucciones:
        if(instruccion[1] == etiqueta):
            return int(instruccion[0]) + 1

    print("Etiqueta no encontrada")
    return -1


def removerEtiquetas(instrucciones):
    contador = 0
    for instruccion in instrucciones:
        if(len(instruccion) == 2):
            instrucciones.pop(contador)
        contador += 1


def indexarInstrucciones(instrucciones):
    contador = 0
    while contador < len(instrucciones):
        instrucciones[contador][0] = contador
        contador += 1
    return instrucciones

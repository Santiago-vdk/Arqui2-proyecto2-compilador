import sys
from Instrucciones import instrucciones_diccionario


def extraerOperandos(line, i):

    if(line.find("//") != -1):
        line = line[0:line.find("//")]
        line = line.split()
    elif(line.find("#") != -1):
        line = line[0:line.find("#")]
        line = line.split()
    else:
        line = line.split()

    # Reemplazo de cada linea las ','
    k = 0
    while k < len(line):
        line[k] = line[k].replace(",", "")

        k += 1

    line.insert(0, i)
    return line


def encontrarEtiqueta(instrucciones, etiqueta):
    for instruccion in instrucciones:
        if(len(instruccion) == 2):
            instruccion_raw = instruccion[-1][0:instruccion[-1].find(":")]
            if(instruccion_raw == etiqueta):
                return int(instruccion[0]) + 1

    print("Encontrar Etiqueta: no encontrada " + etiqueta)
    sys.exit()


def encontrarEtiquetaReIndexadaRelativa(instrucciones, etiqueta, indiceInstruccion):
    for instruccion in instrucciones:
        if(instruccion[1] == etiqueta):
            indiceEtiqueta = instruccion[0]
            nuevaDireccion = int(indiceEtiqueta) - int(indiceInstruccion)
            nuevaDireccion = nuevaDireccion - 1
            return nuevaDireccion

    print("Encontrar Etiqueta: no encontrada " + str(etiqueta))
    sys.exit()


def encontrarEtiquetaReIndexada(instrucciones, etiqueta):
    for instruccion in instrucciones:
        if(instruccion[1] == etiqueta):
            return instruccion[0] + 1

    print("Etiqueta Reindexada no encontrada " + etiqueta)
    sys.exit()


def removerEtiquetas(instrucciones):
    contador = 0
    for instruccion in instrucciones:
        if(len(instruccion) == 2):
            instrucciones.pop(contador)
        contador += 1


def indexarInstrucciones(instrucciones):
    contador = 0
    while contador < len(instrucciones):
        instrucciones[contador].insert(0, contador)
        contador += 1
    return instrucciones


def removerIndicePreTags(instrucciones):
    contador = 0
    while contador < len(instrucciones):
        instrucciones[contador].pop(1)
        contador += 1
    return instrucciones

import os
import sys
from antlr4 import FileStream
from antlr4 import CommonTokenStream
from antlr4 import ParseTreeWalker
from Grammar.GramaticaLexer import GramaticaLexer
from Grammar.GramaticaParser import GramaticaParser
from Grammar.GramaticaListener import GramaticaListener
from Grammar.Listeners import CustomErrorListener
from Parser import *
from Instrucciones import instrucciones_diccionario
from Registros import registros
from Utils import *


def main(argv):

    path = os.getcwd() + '/Programas/'
    programa = path + argv

    input = FileStream(programa, encoding='utf8')
    lexer = GramaticaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GramaticaParser(stream)
    tree = parser.gramatica()
    listen = GramaticaListener()
    walker = ParseTreeWalker()
    walker.walk(listen, tree)

    instrucciones_indexadas = []

    # Parseo en tuplas y lista de instrucciones
    with open(programa) as file:
        contador = 0
        for l in file:
            instrucciones_indexadas.append(extraerOperandos(l, contador))
            contador += 1

    # # Se sustituyen las etiquetas
    posicion = 0
    for instruccion in instrucciones_indexadas:

        # Si la instruccion no es una etiqueta
        if(len(instruccion) > 2):
            nombre_instruccion = instruccion[1].lower()
            valor_instruccion_diccionario = instrucciones_diccionario[nombre_instruccion]

            # Si la instruccion tiene una etiqueta al final
            if(valor_instruccion_diccionario[3] == True):
                etiqueta = instruccion[-1]
                indice = encontrarEtiqueta(
                    instrucciones_indexadas, etiqueta)
                instrucciones_indexadas[posicion][-1] = indice

        posicion += 1

    # Se remueven las etiquetas
    removerEtiquetas(instrucciones_indexadas)

    # Se crea un nuevo indice para las instrucciones
    instrucciones_indexadas = indexarInstrucciones(instrucciones_indexadas)

    # Se reajusta utilizando el primer indice cada instruccion de salto
    posicion = 0
    for instruccion in instrucciones_indexadas:
        nombre_instruccion = instruccion[2].lower()
        valor_instruccion_diccionario = instrucciones_diccionario[nombre_instruccion]
        if(valor_instruccion_diccionario[3] == True):
            direccion = instruccion[-1]
            indice = encontrarEtiquetaReIndexada(
                instrucciones_indexadas, direccion)
            instrucciones_indexadas[posicion][-1] = indice - 1
        posicion += 1

    # Se remueven los indices temporales
    instrucciones_indexadas = removerIndicePreTags(instrucciones_indexadas)

    for instruccion in instrucciones_indexadas:
        print(instruccion)

    instrucciones_compiladas = []

    for instruccion in instrucciones_indexadas:
        nombre_instruccion = instruccion[1].lower()
        valor_instruccion_diccionario = instrucciones_diccionario[nombre_instruccion]
        tipo_instruccion = valor_instruccion_diccionario[1]

        # Se requiere extraer el func
        if(tipo_instruccion == "R"):

            # Los sigueintes valores son binarios
            op_code = valor_instruccion_diccionario[0]
            funct = valor_instruccion_diccionario[2]
            operando_rd = registros[instruccion[2]]
            operando_rs = registros[instruccion[3]]
            operando_rt = registros[instruccion[4]]
            shamt = "00000"
            if(valor_instruccion_diccionario[4] == True):
                shamt = registros[instruccion[3]]
                operando_rs = "00000"

            instruccion_compilada = op_code + operando_rs + \
                operando_rt + operando_rd + shamt + funct

            instrucciones_compiladas.append(instruccion_compilada)

        elif(tipo_instruccion == "I"):
            if(valor_instruccion_diccionario[5] == False):

                # Los siguientes valores son binarios
                op_code = valor_instruccion_diccionario[0]
                funct = valor_instruccion_diccionario[2]
                operando_rs = registros[instruccion[2]]
                operando_rt = registros[instruccion[3]]
                inmediate = str(instruccion[4])

                if(len(inmediate) < 16):
                    inmediate = extender16Bits(inmediate)

                instruccion_compilada = op_code + operando_rs + \
                    operando_rt + inmediate

                instrucciones_compiladas.append(instruccion_compilada)
            else:
                # Los siguientes valores son binarios
                op_code = valor_instruccion_diccionario[0]
                funct = valor_instruccion_diccionario[2]
                operando_compuesto = instruccion[3]

                inmediate = operando_compuesto[0:operando_compuesto.find("(")]
                operando_rt = operando_compuesto[operando_compuesto.find(
                    "(") + 1:operando_compuesto.find(")")]

                operando_rt = registros[operando_rt]

                if(len(inmediate) < 16):
                    inmediate = extender16Bits(inmediate)

                instruccion_compilada = op_code + operando_rs + \
                    operando_rt + inmediate

                instrucciones_compiladas.append(instruccion_compilada)

        elif(tipo_instruccion == "J"):
            # Los siguientes valores son binarios
            op_code = valor_instruccion_diccionario[0]
            funct = valor_instruccion_diccionario[2]
            address = str(instruccion[2])

            if(len(address) < 26):
                address = extender26Bits(address)

            instruccion_compilada = op_code + address

            instrucciones_compiladas.append(instruccion_compilada)
        else:
            print("Error encontrando tipo de instruccion")
            sys.exit()

    for instruccion in instrucciones_compiladas:
        print(instruccion)


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        main("AlgoritmoXOR.asm")
    else:
        main(sys.argv[1])

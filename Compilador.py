import os
from antlr4 import FileStream
from antlr4 import CommonTokenStream
from antlr4 import ParseTreeWalker
from Grammar.GramaticaLexer import GramaticaLexer
from Grammar.GramaticaParser import GramaticaParser
from Grammar.GramaticaListener import GramaticaListener
from Grammar.Listeners import CustomErrorListener
from Parser import *

path = os.getcwd() + '/Programas/'
programa = path + 'Codigo.asm'

input = FileStream(programa)
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

# Se sustituyen las etiquetas
posicion = 0
for instruccion in instrucciones_indexadas:
    if(instruccion[1] in instrucciones_branching):
        etiqueta = instruccion[-1]
        indice = encontrarEtiqueta(instrucciones_indexadas, etiqueta)
        instrucciones_indexadas[posicion][-1] = indice
    posicion += 1

# Se remueven las etiquetas
removerEtiquetas(instrucciones_indexadas)

# Se crea un nuevo indice para las instrucciones
instrucciones_indexadas = indexarInstrucciones(instrucciones_indexadas)

# Se reajusta utilizando el primer indice cada instruccion de salto
posicion = 0
for instruccion in instrucciones_indexadas:
    if(instruccion[2] in instrucciones_branching):
        direccion = instruccion[-1]
        indice = encontrarEtiqueta(instrucciones_indexadas, direccion)
        instrucciones_indexadas[posicion][-1] = "{" + str(indice - 1) + "}"
    posicion += 1

# Se remueven los indices temporales
instrucciones_indexadas = removerIndicePreTags(instrucciones_indexadas)

instrucciones_compiladas = []


for instruccion in instrucciones_indexadas:
    print(instruccion)

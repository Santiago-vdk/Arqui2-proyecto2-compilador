import os
from antlr4 import FileStream
from antlr4 import CommonTokenStream
from antlr4 import ParseTreeWalker
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener
from Listeners import CustomErrorListener
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



# Sustituir etiquetas
posicion = 0
for instruccion in instrucciones_indexadas:
    if(instruccion[1] in instrucciones_branching):
        etiqueta = instruccion[-1]
        indice = encontrarEtiqueta(instrucciones_indexadas, etiqueta)

        instrucciones_indexadas[posicion][-1] = indice
       
    posicion += 1

removerEtiquetas(instrucciones_indexadas)

#instrucciones_indexadas = indexarInstrucciones(instrucciones_indexadas)

for instruccion in instrucciones_indexadas:
    print(instruccion)

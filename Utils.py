import sys
import re


def extender16Bits(binario):
    matches = re.match('[01]*$', binario)
    if(matches):
        bits_faltantes = 16 - len(binario)
        while(bits_faltantes > 0):
            binario = "0" + binario
            bits_faltantes -= 1
        return binario
    else:
        print("Error extendiendo a 16 bits")
        sys.exit()


def extender26Bits(binario):
    matches = re.match('[01]*$', binario)
    if(matches):
        bits_faltantes = 26 - len(binario)
        while(bits_faltantes > 0):
            binario = "0" + binario
            bits_faltantes -= 1
        return binario
    else:
        print("Error extendiendo a 16 bits")
        sys.exit()


def binary(decimal):
    otherBase = ""
    while decimal != 0:
        otherBase = str(decimal % 2) + otherBase
        decimal //= 2
    return otherBase

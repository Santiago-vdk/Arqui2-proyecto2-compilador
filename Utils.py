import sys
import re


def extender5Bits(binario):
    matches = re.match('[01]*$', binario)
    if(matches):
        bits_faltantes = 5 - len(binario)
        while(bits_faltantes > 0):
            binario = "0" + binario
            bits_faltantes -= 1
        return binario
    else:
        print("Error extendiendo a 5 bits")
        sys.exit()


def extender16Bits(binario):
    # print(binario)
    # if(binario[0] == '-'):
    #     print(binario)
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


def twosComplement(value, bitLength):
    return bin(value & (2**bitLength - 1))


def extender16BitsNegativos(binario):

    matches = re.match('[01]*$', binario[1:len(binario)])
    if(matches):
        binario = binario[1:len(binario)]
        bits_faltantes = 16 - len(binario)

        while(bits_faltantes > 0):
            binario = "1" + binario
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

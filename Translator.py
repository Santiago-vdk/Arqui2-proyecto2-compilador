import sys


def traducirOperando(registro):

    if(registro == "$0"):

        return "00000"
    elif(registro == "$1"):

        return "00001"
    elif(registro == "$2"):

        return "00010"
    elif(registro == "$3"):

        return "00011"
    elif(registro == "$4"):

        return "00100"
    elif(registro == "$5"):

        return "00101"
    elif(registro == "$6"):

        return "00110"
    elif(registro == "$7"):

        return "00111"
    elif(registro == "$8"):

        return "01000"
    elif(registro == "$9"):

        return "01001"
    elif(registro == "$10"):

        return "01010"
    elif(registro == "$11"):

        return "01011"
    elif(registro == "$12"):

        return "01100"
    elif(registro == "$13"):

        return "01101"
    elif(registro == "$14"):

        return "01110"
    elif(registro == "$15"):

        return "01111"
    elif(registro == "$16"):

        return "10000"
    elif(registro == "$17"):

        return "10001"
    elif(registro == "$18"):

        return "10010"
    elif(registro == "$19"):

        return "10011"
    elif(registro == "$20"):

        return "10100"
    elif(registro == "$21"):

        return "10101"
    elif(registro == "$22"):

        return "10110"
    elif(registro == "$23"):

        return "10111"
    elif(registro == "$24"):

        return "11000"
    elif(registro == "$25"):

        return "11001"
    elif(registro == "$26"):

        return "11010"
    elif(registro == "$27"):

        return "11011"
    elif(registro == "$28"):

        return "11100"
    elif(registro == "$29"):

        return "11101"
    elif(registro == "$30"):

        return "11110"
    elif(registro == "$31"):

        return "11111"
    else:
        print("Registro no encontrado")
        sys.exit()


def traducirOperacion(operacion):
    if(operacion == "add"):

        return "00000"
    elif(operacion == "addi"):

        return "00001"
    elif(operacion == "sub"):

        return "00010"
    elif(operacion == "subi"):

        return "00011"
    elif(operacion == "j"):

        return "10011"
    elif(operacion == "bne"):

        return "10100"
    elif(operacion == "beq"):

        return "10101"
    elif(operacion == "mult"):

        return "10110"
    elif(operacion == "lb"):

        return "01010"
    elif(operacion == "sb"):

        return "01100"
    elif(operacion == "mov"):

        return "01110"
    elif(operacion == "movi"):

        return "01111"
    else:
        print("Operacion no encontrada")
        sys.exit()

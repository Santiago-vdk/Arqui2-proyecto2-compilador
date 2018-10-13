def extender16Bits(binario):
    bits_faltantes = 16 - len(binario)
    while(bits_faltantes > 0):
        binario = "0" + binario
        bits_faltantes -= 1
    return binario


def extender26Bits(binario):
    bits_faltantes = 26 - len(binario)
    while(bits_faltantes > 0):
        binario = "0" + binario
        bits_faltantes -= 1
    return binario

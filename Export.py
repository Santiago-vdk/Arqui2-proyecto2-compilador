import os

path = os.getcwd() + '/ProgramasBin/'


def ExportMIF(instrucciones, nombrePrograma):

    archivo_rom = nombrePrograma[0:nombrePrograma.find(".")] + ".mif"

    # Creacion de la memoria
    f = open(path + archivo_rom, 'w')
    f.write('WIDTH=32;\n')
    f.write('DEPTH = 65536;\n')
    f.write('\n')
    f.write('ADDRESS_RADIX = UNS;\n')
    f.write('DATA_RADIX = BIN;\n')
    f.write('\n')
    f.write('CONTENT BEGIN\n')
    f.close()

    i = 0
    with open(path + archivo_rom, 'a') as file:
        while(i < len(instrucciones)):
            file.write("       " + str(i) + " : " + instrucciones[i] + ";\n")
            i += 1
        file.close()

    f = open(path + archivo_rom, 'a')
    f.write("       [" + str(i) + ".." + str(65535) + "] : " +
            "00000000000000000000000000000000;\n")
    f.write("END;")
    f.close()

    return archivo_rom


def ExportMem(instrucciones, nombrePrograma):

    archivo_mem = nombrePrograma[0:nombrePrograma.find(".")] + ".mem"

    i = 0
    with open(path + archivo_mem, 'a') as file:
        while(i < len(instrucciones)):
            file.write("    " + "mem[" + str(i) + "]" +
                       " = 32'b" + instrucciones[i] + ";\n")
            i += 1
        file.close()

    return archivo_mem

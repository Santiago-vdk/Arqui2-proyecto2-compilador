
# archivo_rom = "C:/repo/proyecto_1_arqui_1/Compilador/ROM.mif"

# # Creacion de la memoria
# f = open(archivo_rom, 'w')
# f.write('WIDTH=32;\n')
# f.write('DEPTH = 65536;\n')
# f.write('\n')
# f.write('ADDRESS_RADIX = UNS;\n')
# f.write('DATA_RADIX = BIN;\n')
# f.write('\n')
# f.write('CONTENT BEGIN\n')
# f.close()

# z = 0
# while(z < len(instrucciones_binary)):
#     with open(archivo_rom, 'a') as the_file:
#         the_file.write("       " + str(z) + " : " +
#                        instrucciones_binary[z] + ";\n")

#     z += 1
# f = open(archivo_rom, 'a')
# f.write("       [" + str(z) + ".." + str(65535) + "] : " +
#         "10111000000000000000000000000000;\n")
# f.write("END;")
# f.close()

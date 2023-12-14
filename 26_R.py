# 26. Escribir un programa que lea un archivo de texto llamado carta.txt. Tenemos que
# contar los caracteres, las líneas y las palabras. Para simplificar, supondremos que cada
# palabra está separada de otra por un único espacio en blanco o por un salto de línea.

f = open('carta.txt', 'r')
caracteres, lineas, palabras = 0, 0, 0

while True:
    linea = f.readline().strip()
    if linea == '':
        break
    caracteres += len(linea)
    lineas += 1
    palabras += linea.count(' ') + 1

f.close()
print('El documento tiene', lineas, 'lineas,', palabras, 'palabras y', caracteres, 'letras')

# 26. Escribir un programa que lea un archivo de texto llamado carta.txt. Tenemos que
# contar los caracteres, las líneas y las palabras. Para simplificar, supondremos que cada
# palabra está separada de otra por un único espacio en blanco o por un salto de línea.

a = open('carta.txt', 'r')
f = a.readlines()
a.close()

f = [x.strip() for x in f]
lineas = len(f)                                     #Cuenta las líneas
palabras = sum([x.count(' ') for x in f]) + lineas  #Cuenta las palabras
letras = sum([len(x) for x in f])                   #Cuenta las letras

print('El documento tiene', lineas, 'lineas,', palabras, 'palabras y', letras, 'letras')

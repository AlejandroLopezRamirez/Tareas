# 22. Escribir un programa que solicite al usuario el nombre de un archivo de texto y muestre
# su contenido en pantalla. Si no se proporciona ningún nombre de archivo, el programa
# usará por defecto prueba.txt.

name = input('Introduzca el nombre del archivo que desea ver: ')

name = name if name != '' else 'prueba.txt'

a = open(name, 'r')
f = a.readlines()
a.close()

f_separada = [x.strip() for x in f]
resultado = [print(x) for x in f_separada]

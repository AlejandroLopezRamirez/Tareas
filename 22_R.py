# 22. Escribir un programa que solicite al usuario el nombre de un archivo de texto y muestre
# su contenido en pantalla. Si no se proporciona ningún nombre de archivo, el programa
# usará por defecto prueba.txt.

nombre = input('Introduzca el nombre del archivo que desea ver: ')

if nombre == '':
    nombre = 'prueba.txt'

try:
    with open(nombre, 'r') as a:
        f = a.readlines()

    f_separada = [x.strip() for x in f]
    resultado = [print(x) for x in f_separada]
except FileNotFoundError:
    print('Archivo no encontrado')

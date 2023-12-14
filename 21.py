# 21. Escribir un programa que duplique el contenido de un archivo cuyo nombre se pide al
# usuario. El archivo copia tendrá el mismo nombre con el prefijo «copia_de_».

name = input('Introduzca el nombre del archivo que desea copiar: ')

a = open(name, 'r')
f = a.readlines()
a.close()

a2 = open('copia de ' + name, 'w')

f2 = a2.writelines(f)

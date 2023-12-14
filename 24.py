# 24. Escribir un programa que pida al usuario su nombre y su edad. Esos datos deben
# guardarse en el archivo datos.txt. Si ese archivo existe, debe añadirse al final en una
# nueva línea, y en caso de no existir, debe crearse.

name = input('Introduzca su nombre: ')
age = input('Introduzca su edad: ')

a = open('datos.txt', 'a')
a.write(name + ' ' + age + '\n')
a.close()

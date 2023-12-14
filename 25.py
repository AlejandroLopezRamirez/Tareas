# 25. Escribir un programa que lea dos listas de números enteros no ordenados de sendos
# archivos con un número por línea, los reúna en una lista única y los guarde en orden
# creciente en un tercer archivo, de nuevo uno por línea.

a = open('lista1.txt', 'r')
l1 = a.readlines()
a.close()

a = open('lista2.txt', 'r')
l2 = a.readlines()
a.close()

l = l1 + l2                             #Aquí concatena las dos listas
l = [x.strip() for x in l]              #Aquí elimina el \n
l = [float(x) for x in l]               #Aquí convierte los str en float para poder operar
l = sorted(l)                           #Aquí ordena la lista devolviendo otra lista
l = [str(x) for x in l]                 #Aquí reconvierte a string
l = [x + '\n' for x in l]               #Aquí le añade el salto de linea

a = open('lista.txt', 'w')
a.writelines(l)
a.close()

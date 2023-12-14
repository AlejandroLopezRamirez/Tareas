# 8. Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
# introducidos por teclado.

suma = 0
cont = 0

while cont != 5:
    n = float(input('Introduza un número: '))
    suma = suma + n
    cont += 1
print('La media de las', cont, 'notas es:', suma / cont)

# 6. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
# comprendido entre 0 y 10, introducido por teclado.

n = int(input('Introduzca un número: '))

cont = 0

while cont < 11:
    print(n, 'x', cont, '=', n * cont)
    cont += 1

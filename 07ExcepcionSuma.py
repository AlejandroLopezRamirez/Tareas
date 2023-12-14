import sys

intentos = 0
while True:
    intentos += 1
    if intentos > 3:
        print('Me cansé')
        sys.exit(1)
    try:
        x = int(input('Introduzca el primer número: '))
        break
    except ValueError:
        print('El primer dato introducidono no es un número entero.')

intentos = 0
while True:
    intentos += 1
    if intentos > 3:
        print('Me cansé')
        sys.exit(1)
    try:
        y = int(input('Introduzca el segundo número: '))
        break
    except ValueError:
        print('El segundo dato introducidono no es un número entero.')

print('El resultado es:', x + y)

import re

num = input('Introduzca un número real: ')
correcto = re.compile(r'^\d+([.,]\d+)?$')
if correcto.search(num) is None:
    print('Error: el numero es incorrecto')
    exit(1)
separador = re.compile(r'[.,]')
partes = separador.split(num)
numero = float('.'.join(partes))
print('El número es', numero)

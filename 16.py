# 16. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
# comprendido entre 0 y 10, introducido por teclado.

import sys

print(tuple(map(lambda x: int(sys.argv[1]) * x, range(11))))

n = int(sys.argv[1])
tuple(print(tuple( n * x for x in range(11))))

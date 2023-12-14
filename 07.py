# 7. Escribir un programa que pida dos
# números al usuario: a y b.
# Deberá mostrar Sí si ambos números son iguales
# y No en caso contrario.

import sys

igual = int(sys.argv[1]) == int(sys.argv[2])

print('Sí' if igual else 'No')

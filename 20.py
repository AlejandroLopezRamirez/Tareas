# 20. Crear un archivo de texto con una colección de números reales, uno por línea.

# A continuación, escribir un programa que:
# a. Abra el archivo para lectura.
# b. Lea todas sus líneas.
# c. Muestre finalmente la suma de todos ellos.

from functools import reduce

suma = lambda x, y: float(x) + float(y)

a = open('numeros_reales_linea.txt', 'r')
f = a.readlines()
a.close()

resultado = reduce(suma, f)

print('El resultado es', resultado)

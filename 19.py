# 19. Crear el archivo de texto «numeros_reales.txt» en el directorio de trabajo
# actual que contenga una sola línea de texto con números reales separados por espacios.
# A continuación, escribir un programa que abre ese archivo, lea los números que contiene
# y calcule la suma y la media aritmética, mostrando los resultados por pantalla.

from functools import reduce

suma = lambda x, y: float(x) + float(y)

a = open('numeros_reales.txt', 'r')
f = a.readlines()
a.close()

# Aquí volcamos el contenido del fichero en f (es una lista con un string)

f = f[0].split()

# Aquí convertimos la lista de un elemento a una lista con varios elementos

resultado = reduce(suma, f)
media = resultado / len(f)

print('El resultado es', resultado, 'y la media es', media)

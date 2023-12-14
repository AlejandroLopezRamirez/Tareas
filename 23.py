# 23. Hacer el mismo ejercicio anterior, pero recogiendo el nombre del archivo desde la línea
# de órdenes del sistema operativo. (Indicación: usar sys.argv)

from sys import argv

name = str(argv[1]) if len(argv) == 2 else 'prueba.txt'

a = open(name, 'r')
f = a.readlines()
a.close()

f_separada = [x.strip() for x in f]
resultado = [print(x) for x in f_separada]

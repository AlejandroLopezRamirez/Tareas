# 27. En el archivo numeros.txt disponemos de una serie de números (uno por línea). Diseñar
# un programa que procese el archivo y nos muestre el menor y el mayor.

a = open('numeros.txt', 'r')
f = a.readlines()
a.close()

f = [x.strip() for x in f]
f = [int(x) for x in f]
print('El número más pequeño es', str(min(f)) + ',' , 'y el número más grande es', max(f))

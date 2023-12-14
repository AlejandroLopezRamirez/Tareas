# Escribe un programa que solicite al usuario un número y
# le indique si es par (mediante un mensaje Sí o No).

par = lambda x: x % 2 == 0

num = int(input('Introduce un número: '))
print ('Sí' if par(num) else 'No')

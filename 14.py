# 14. Escribir un programa que pida al usuario su edad y que imprima el
# mensaje «¡Qué joven!» si es menor de 25 años y «No está mal.» si tiene entre 25 y 40 años.

edad = int(input('Introduzca su edad: '))

print('¡Qué joven!\n' if edad < 25 else 'No está mal.\n'\
       if edad < 40 else '', end = '')

# 12. Escribir un programa que pida al usuario su edad y que imprima el
# mensaje «¡Qué joven!» si es menor de 25 años.

edad = int(input('Introduzca su edad: '))

print('¡Qué joven!\n' if edad < 25 else '', end = '')

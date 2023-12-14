# 13. Escribir un programa que pida al usuario su edad y que imprima el
# mensaje «¡Qué joven!» si es menor de 25 años y «¡Qué mayor!» en caso contrario.

edad = int(input('Introduzca su edad: '))
print('¡Qué joven!' if edad < 25 else '¡Qué mayor!')

# 3. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
# joven!» si es menor de 25 años y «¡Qué mayor!» en caso contrario.

age = int(input('Introduzca su edad: '))

if age < 25:
    print('¡Qué joven!')
else:
    print('¡Qué mayor!')

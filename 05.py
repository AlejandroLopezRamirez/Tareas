# 5. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
# joven!» si es menor de 25 años, «No está mal.» si tiene entre 25 y 40 años y «¡Qué
# mayor!» si tiene más de 40 años.

age = int(input('Introduzca su edad: '))
if age < 25:
    print('¡Qué joven!')
elif age in range(25, 41):
    print('No está mal')
elif age > 40:
    print('¡Qué mayor!')

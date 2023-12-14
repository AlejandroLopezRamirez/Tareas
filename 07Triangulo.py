'''
Pedir por consola un númeron y dibujar un triángulo
rectángulo de n elementos de lado, utilizando para ello
asteriscos (*). Por ejemplo, para n = 4:
* * * *
* * *
* *
*
'''

while True:
    try:
        n = int(input('Introduzca un número'))
    except ValueError:
        print('El dato introducido es incorrecto')

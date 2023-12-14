# 12. Escribir un programa que gestione datos almacenados en una lista, de forma que muestre
# un menú con las siguientes opciones:

# 1. Añadir un elemento a la lista.
# 2. Cambiar el valor de un elemento de la lista.
# 3. Eliminar un elemento de la lista.
# 4. Eliminar todos los elementos de la lista.
# 5. Mostrar los elementos de la lista.
# 0. Salir del programa.

# El programa deberá pedir la información necesaria para cada opción elegida por el
# usuario.
import sys

option = 6
l = []

while True:
    print('1. Añadir un elemento a la lista.')
    print('2. Cambiar el valor de un elemento de la lista.')
    print('3. Eliminar un elemento de la lista.')
    print('4. Eliminar todos los elementos de la lista.')
    print('5. Mostrar los elementos de la lista.')
    print('0. Salir del programa.')
    option = int(input('¿Qué quieres hacer? '))

    if option == 1:
        concatena = input('¿Qué elemento quieres añadir? ')
        l.append(concatena)

    elif option == 2:
        cambiaE = input('¿Qué elemento quieres añadir? ')
        cambiaN = int(input('¿Dónde está el elemento que quieres sutituir? '))
        l[cambiaN] = cambiaE

    elif option == 3:
        borra = int(input('¿Qué elemento quieres borrar? '))
        del l[borra]

    elif option == 4:
        l = []

    elif option == 5:
        print(l)
        input()

    elif option == 0:
        print('Saliendo')
        sys.exit(1)

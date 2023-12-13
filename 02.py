'''
Escribir en Python una función completar() sin parámetros que lea un
archivo de texto llamado «datos.txt» con un texto similar a éste:

1249378
*********
32584*9

En cada línea del texto habrá una cadena de 9 caracteres formada por
dígitos y asteriscos, de forma que los dígitos no se pueden repetir
y puede haber muchos asteriscos (siempre que no se sobrepase la
longitud máxima de 9 caracteres en la línea).

La función deberá modificar el contenido del archivo, sustituyendo
los asteriscos por los dígitos que falten en esa línea, completando
de menor a mayor, de la siguiente forma:

124593678
123456789
132658479

De forma que:
- En la primera línea se han sustituido los asteriscos por 5 y 6
(en ese orden)
- En la segunda línea se han sustituido por todos los dígitos del
1 al 9 (en ese orden)
- En la tercera línea se han sustituido por 1, 6 y 7 (en ese orden).

Observación: Antes de cada test, se llama a completar() y luego se
almacena el contenido del archivo «datos.txt» en la lista lineas
(en cada elemento de la lista se guarda una línea del archivo),
eliminando los saltos de línea finales de cada línea.
'''

def completar():
    '''
    Que haga lo de arriba
    '''
    linea = ' '
    f = open('datos.txt', 'r+' )
    while linea !='':
        linea = f.readline()
        i = 1
        while '*' in linea:
            if str(i) in linea:
                i += 1
            else:
                linea = linea.replace('*', str(i), 1)
                i += 1
        linea = linea + '\n'
        f.close()
        w = open('datos.txt', 'w')
        w.write(linea)
        w.close()

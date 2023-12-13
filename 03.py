'''
Escribir una función ahorcado(prueba) que juegue un turno del juego del ahorcado.
Para ello, la función recibe una cadena (el intento) con la palabra que el usuario
cree que es la que hay que averiguar (la solución). La solución se encuentra almacenada
en la primera línea del archivo de texto «ahorcado.txt». La función deberá leer ese archivo
y comprobar si el intento coincide con la solución. En caso afirmativo, deberá mostrar por
la salida el mensaje «¡Enhorabuena!». En caso contrario, deberá mostrar la solución con las
letras adivinadas (es decir, las letras que aparecen en el intento), y las letras no adivinadas
sustituidas por un guión bajo. Se supone que las letras son siempre mayúsculas y sin acentos.

Por ejemplo, si la solución es la palabra «INFORMATICA», tenemos:

>>> ahorcado('MANZANA')
_N___MA___A
>>> ahorcado('MATEMATICAS')
_____MATICA
>>> ahorcado('INFORMATICA')
¡Enhorabuena!
'''
def ahorcado(prueba):
    '''
    Hace lo que pide el ejercicio
    '''
    f = open('ahorcado.txt', 'r')
    solucion = f.readline().strip()
    f.close()
    cont = len(solucion)
    respuesta = ''

    if solucion == prueba:
        return '¡Enhorabuena!'
    while cont > 0:
        respuesta += '_'
        cont -= 1


    while len(solucion) > 0:
        cont = 0
        if solucion[0] in prueba:
            respuesta = respuesta.replace(respuesta[cont], solucion[0])
            print(respuesta)
            input()
        solucion = solucion[1:]
        cont += 1
    return respuesta

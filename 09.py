# 9. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
# luego las muestre en orden inverso a como se han introducido, desde la última cadena
# introducida hasta la primera.

# Indicación: Usar el método append sobre la lista y luego un bucle que recorra la lista
# desde el último elemento hasta el primero.
l = []
while len(l) != 10:
    l.append((input('Intoduzca una cadena: ')))
while len(l) != 0:
    print(l.pop(-1))

# 18. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
# luego las muestre en orden inverso a como se han introducido, desde la última cadena
# introducida hasta la primera.

# Indicación: Usar el método append sobre la lista y luego un bucle que
# recorra la lista desde el último elemento hasta el primero.

l = []

l.append(input('Introduzca el elemento 1: '))
l.append(input('Introduzca el elemento 2: '))
l.append(input('Introduzca el elemento 3: '))
l.append(input('Introduzca el elemento 4: '))
l.append(input('Introduzca el elemento 5: '))
l.append(input('Introduzca el elemento 6: '))
l.append(input('Introduzca el elemento 7: '))
l.append(input('Introduzca el elemento 8: '))
l.append(input('Introduzca el elemento 9: '))
l.append(input('Introduzca el elemento 10: '))

invierte_rec = lambda lista, issue, acc: acc if len(acc) == 10 else\
                                   invierte_rec(lista[:9], acc.append(l[-1]), acc)

print(invierte_rec(l, None, []))

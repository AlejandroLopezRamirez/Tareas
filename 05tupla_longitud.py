#Función que calcula cuantos elementos contiene una tupla

longitud_rec = lambda t: 0 if t == () else 1 + longitud_rec(t[1:])


longitud_iter = lambda t, cont: cont if t == () else longitud_iter(t[1], cont +1)

longitud = lambda t: longitud_iter(t, 0)

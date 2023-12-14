#Mete una tupla de ints y saca la media, primero saca la longitud para poder hacerlo

media_rec = lambda t, acc, cont: acc / cont if t == () else media_rec(t[1:], acc + t[0], cont + 1)

media = lambda t: media_rec(t, 0, 0)

#Recibe una tupla y devuelve la suma de todos los elementos de la tupla

# | Pre:    tuple[int] (Todos los elementos de la tupla son de tipo int)
# {         suma_tupla(t:tuple) -> tuple
# | Post:   suma_tupla(t) = la suma de los elementos de t

suma_tupla_rec = lambda t: 0 if t == () else t[0] + suma_tupla_rec(t[1:])

suma_tupla_iter = lambda t, acc: acc if t == () else suma_tupla_iter(t[1:], acc + t[0])

suma = lambda t: suma_tupla_iter(t, 0)

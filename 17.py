# 17. La función rota tiene la siguiente especificación:

# | Pre :   n> = 0
# {         rota(n:int, t:tuple) -> tuple
# | Post :  rota(n, t) = la tupla obtenida poniendo los n primeros elementos de t al final

# Por ejemplo: rota(1, (3, 2, 5, 7)) == (2, 5, 7, 3)
# Por ejemplo: rota(2, (3, 2, 5, 7)) == (5, 7, 3, 2)
# Por ejemplo: rota(3, (3, 2, 5, 7)) == (7, 3, 2, 5)

# Escribir una función recursiva que satisfaga dicha especificación.

insertar = lambda t, e, p: (e,) if t == () else \
                           (e,) + t if p == 0 else \
                           (t[0],) + insertar(t[1:], e, p - 1)

rota = lambda n, t: () if t == () else \
                    t if n == 0 else \
                    insertar(rota(n-1, t[1:]), t[0], len(t) - n)

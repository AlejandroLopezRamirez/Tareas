# 18. La función rota1 tiene la siguiente especificación:

# | Pre :   n> = 0
# {         rota1(t:tuple) -> tuple
# | Post :  rota1(t) = la tupla obtenida poniendo el primer elemento de t al final

# Por ejemplo: rota1((3, 2, 5, 7)) == (2, 5, 7, 3)

# Escribir una función recursiva que satisfaga dicha especificación.

insertar = lambda t, e, p: (e,) if t == () else \
                           (e,) + t if p == 0 else \
                           (t[0],) + insertar(t[1:], e, p - 1)

rota = lambda n, t: () if t == () else \
                    t if n == 0 else \
                    insertar(rota(n-1, t[1:]), t[0], len(t) - n)

rota1 = lambda t: rota(1, t)

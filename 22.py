# 22. La función finales tiene la siguiente especificación:

# | Pre :   n >= 0
# {         finales(n: int, t: tuple) -> tuple
# | Post :  finales(n,t) = la tupla que contiene los n elementos finales de t

# Por ejemplo: finales(2, (1, 2, 3, 4)) == (3, 4)

# Escribir una función recursiva que satisfaga dicha especificación.

finales = lambda n, t: t if len(t) == n else finales(n, t[1:])

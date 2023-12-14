# 12. La función sustituye tiene la siguiente especificación:

# | Pre :   True
# {         sustituye(a, b, t: tuple) -> tuple
# | Post :  sustituye(a, b, 𝑡) = una tupla igual que t pero
#                                sustituyendo los a por b


# Escribir una función recursiva que satisfaga dicha especificación y que genere un
# proceso:

# a) recursivo.

aux = lambda x, y, z: (y,) if x != y else (z,)

sustituye_rec = lambda a, b, t: () if t == () else \
                        aux(a, t[0], b) + sustituye_rec(a, b, t[1:])

# b) iterativo.

sustituye_iter = lambda a, b, t, acc: acc if t == () else \
                                sustituye_iter(a, b, t[1:], acc + aux(a, t[0], b))

sustituye = lambda a, b, t: sustituye_iter(a, b, t, ())

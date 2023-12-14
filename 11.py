# 11. La función quita tiene la siguiente especificación:

# | Pre :   True
# {         quita(e, t: tuple) -> tuple
# | Post :  quita(𝑒, 𝑡) = una tupla igual que t pero sin los e


# Escribir una función recursiva que satisfaga dicha especificación y que genere un
# proceso:

# a) recursivo.

aux = lambda x, y: (y,) if x != y else ()

quita_rec = lambda e, t: () if t == () else \
                        aux(e, t[0]) + quita_rec(e, t[1:])

# b) iterativo.

quita_iter = lambda e, t, acc: acc if t == () else \
                                quita_iter(e, t[1:], acc + aux(e, t[0]))

quita = lambda e, t: quita_iter(e, t, ())

# 10. La función cuantos tiene la siguiente especificación:

# | Pre :   True
# {         cuantos(e, t: tuple) -> int
# | Post :  cuantos(𝑒, 𝑡) = el número de veces que aparece e en t


# Escribir una función recursiva que satisfaga dicha especificación y que genere un
# proceso:

# a) recursivo.

aux = lambda x, y: 1 if x == y else 0

cuantos_rec = lambda e, t, : 0 if t == () else\
                               aux(e, t[0]) + cuantos_rec(e, t[1:])

# b) iterativo.

cuantos_it = lambda e, t, acc: acc if t == () \
                                   else cuantos_it(e, t[1:], acc + 1) \
                                        if e == t[0] \
                                        else cuantos_it(e, t[1:], acc)

cuantos = lambda e, t: cuantos_it(e, t, 0)

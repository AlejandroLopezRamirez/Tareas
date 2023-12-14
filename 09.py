# 9. La función elem tiene la siguiente especificación:

# | Pre :   True
# |         elem(𝑒, 𝑡:tuple) -> bool
# {
# |                     | True si e está en t
# | Post :  elem(𝑒, 𝑡) ={
#                       | False en caso contrario


# Escribir una función recursiva que satisfaga dicha especificación.

elem = lambda e, t: True if e == () else \
                    elem (e[1:], t) if e[0] in t \
                    else False

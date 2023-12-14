# 20. La función mayor tiene la siguiente especificación:

# | Pre :   t != ()
# {         mayor(t:tuple[𝛼]) -> 𝛼
# | Post :  mayor(t) = el mayor elemento de t

# Por ejemplo: mayor((3, 2, 5, 7)) == 7

# Escribir una función recursiva que satisfaga dicha especificación.

mayor = lambda t: max(t[0], mayor(t[1:]))

# 13. La función ultimo tiene la siguiente especificación:

# | Pre :   t ≠()
# {         ultimo(𝑡:tuple)
# | Post :  ultimo(𝑡) = el último elemento de t


# Escribir una función recursiva que satisfaga dicha especificación.

ultimo = lambda t: t[0] if t[1:] == () else ultimo(t[1:])

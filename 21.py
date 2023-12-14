# 21. La función menor_mayor tiene la siguiente especificación:

# | Pre :   t != ()
# {         menor_mayor(t:tuple[𝛼]) -> tuple[𝛼]
# | Post :  menor_mayor(t) = una tupla con dos elementos que contiene el menor y
# |                          el mayor elemento de t, en ese orden

# Por ejemplo: menor_mayor((3, 2, 5, 7)) == (2, 7)

# Escribir una función recursiva que satisfaga dicha especificación.

aux = lambda t, me, ma: (me, ma) if t == () else \
        aux(t[1:], min(t[0], me), max(t[0], ma))

menor_mayor = lambda t: aux(t, t[0], t[0])

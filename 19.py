# 19. La función menor tiene la siguiente especificación:

# | Pre :   t != ()
# {         menor(t:tuple[𝛼]) -> 𝛼
# | Post :  menor(t) = el menor elemento de t

# Por ejemplo: menor((3, 2, 5, 7)) == 2

# Escribir una función recursiva que satisfaga dicha especificación.

menor = lambda t: min(t[0], menor(t[1:]))

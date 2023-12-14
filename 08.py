# 8. La función par determina si un número entero (positivo o negativo) es par:
# par(0) = True
# par(1) = False
# par(-27) = False
# Se pide:

# a) Escribir su especificación.

"""
#            | Pre:      n ∈ ℕ
# par(n) =   {           par (n: int) -> bool
#            | Post:     par (n) par = True
#                                impar = False
"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

par = lambda n: True if n == 0 else \
                        not par(abs(n) - 1)

# c) ¿Cómo se podría implementar una función impar a partir de la función par?

impar = lambda n: not par(n)

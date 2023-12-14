# 7. La función par_positivo determina si un número entero positivo es par:

# par_positivo(0) = True
# par_positivo(1) = False
# par_positivo(27) = False
# par_positivo(82) = True

# Se pide:
# a) Escribir su especificación.

"""
#                   | Pre:      a >= 0
# par_positivo(n) = {           par_positivo(n: int) -> bool
#                   | Post:     par_positivo(n) par = True
#                                               impar = False
"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

par_positivo = lambda n: True if n == 0 else \
                         not par_positivo(n - 1)

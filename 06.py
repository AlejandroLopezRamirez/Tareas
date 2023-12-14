# 6. La función voltea le da la vuelta a un número entero:
# voltea(423) = 324
# voltea(7) = 7
# Se pide:
# a) Escribir su especificación.

"""
#             | Pre:      digitos(n) >= 1
# voltea(n) = {           voltea(n: int) -> int
#             | Post:     voltea(n) -> n volteado
"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

digito = lambda n: 1 if n < 10 else 1 + digito(n//10)

voltea = lambda n: n if n < 10 else voltea(n//10) + (n%10) * (10 ** digito(n // 10))

# Indicación: Usar la función digitos que devuelve la cantidad de dígitos que tiene un
# entero. Usar además la indicación del ejercicio anterior.

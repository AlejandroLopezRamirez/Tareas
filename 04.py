# 4. La suma lenta es un algoritmo para sumar dos números para el que sólo necesitamos
# saber cuáles son el anterior y el siguiente de un número dado. El algoritmo se basa en
# la siguiente recurrencia:

#                       | b                             si a = 0
# suma_lenta(a, b) =    {
#                       | suma_lenta(ant(a), sig(b))    si a > 0

# Suponiendo que tenemos las siguientes funciones ant y sig:
ant = lambda n: n - 1
sig = lambda n: n + 1

# Se pide:
# a) Escribir su especificación.
"""
#                       | Pre:      a >= 0
# suma_lenta (a, b) =   {           suma_lenta (a: int, b:int) -> int
#                       | Post:     suma_lenta (a, b) = a + b
"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

suma_lenta = lambda a, b: b if a == 0 else suma_lenta(ant(a), sig(b))

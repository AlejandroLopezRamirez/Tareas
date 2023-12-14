#1. Escribir en forma de función todos los programas solicitados en el boletín de ejercicios
#   de «Programación funcional (I)». Para cada una de ellas, dar un ejemplo de uso.

#05

aprox = lambda long_tibia, sexo: \
        (69.089 + 2.232 * long_tibia) if sexo == "V" else \
        (61.412 + 2.317 * long_tibia)

altura = lambda long_tibia, sexo, edad: \
            aprox(long_tibia, sexo) - \
                (0.06* (edad -29) if edad >= 30 else 0)

"""
Ejemplo de uso:
>>> altura(20, "V", 35)
113.369
"""

#06

from math import pi

volumen = lambda r: (4/3) * pi * (r ** 3)
"""
Ejemplo de uso:
>>> volumen(2)
33.510
"""

#07

igual_3 = lambda a, b, c: (a == b) and (b == c)

"""
Ejemplo de uso:
>>> igual_3(1, 1, 1)
True
"""


#08

igual_4 = lambda a, b, c, d: igual_3(a, b, c) and c == d

"""
Ejemplo de uso:
>>> igual_4(2, 2, 2, 2)

"""


#09

orden_2 = lambda d1, d2: str(d1) + " " + str(d2) if d1 <= d2 else str(d2) + " " + str(d1)

"""
Ejemplo de uso:
>>>

"""


#10

OYE = "AUN TIENES ESTO PENDIENTE"

"""
Ejemplo de uso: esto está pendiente
>>>

"""

#11-a

from math import lcm, gcd

mcm = lcm

"""
Ejemplo de uso:
>>> mcm(4, 6)
12
"""

#11-b

mcmb = lambda num_1, num_2: (num_1 * num_2) // gcd(num_1, num_2)

"""
Ejemplo de uso:
>>> mcmb(4, 6)
12
"""


#12

union = lambda cadena: cadena.replace(" ", "")

"""
Ejemplo de uso:
>>> union("Esto es una prueba")
Estoesunaprueba
"""

#13

igual = lambda s1, s2: s1.lower() == s2.lower()

"""
Ejemplo de uso:
>>> igual("Hola", "hOla")
True
"""

#14

sin_tildes = lambda s: s.translate(str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU"))

"""
Ejemplo de uso:
>>> sin_tildes("¡Ramón! ¡Cuánto tiempo! ¿Cómo estás?")
"¡Ramon! ¡Cuanto tiempo! ¿Como estas?"
"""

#15

sanear = lambda s : union(sin_tildes(s.lower()))

es_palindromo = lambda s: sanear(s) == sanear(s) [::-1]

"""
Ejemplo de uso:
>>> "Dábale arroz a la zorra el abad"
True
"""

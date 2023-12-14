#5. La función suma_digitos calcula la suma de los dígitos de un número entero:
#       suma_digitos(423) = 4 + 2 + 3 = 9
#       suma_digitos(7) = 7

# Se pide:

# a) Escribir su especificación.
"""
        Pre: True
                suma_digitos(n: int) --> int

        Post: suma_digitos(n) = la suma de los dígitos de n AND
              suma_digitos(n) >= 0
"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

"""
suma_digitos(423) =
= si yo supiera calcular 3 + suma_digitos(42)

suma_digitos(n) = el ultimo dígito de n + suma_digitos(n quitandole el ultimo dígito)
"""

#suma_digitos = lambda n: abs(n) if abs(n) < 10 else (abs(n) % 10) + suma_digitos(abs((n) // 10))

"""
                    abs(n) si abs(n) < 10
suma_digitos(n)={
                    (abs(n) % 10) + suma_digitos(abs(n) // 10)
"""

suma_digitos = lambda n: suma_aux(abs(n))

suma_aux = lambda n: n if n < 10 else \
                     (n % 10) + suma_aux(n // 10)

# Indicación: Recordar que n // 10 le quita el último dígito a 𝑛. Además, n % 10 devuelve
# el último dígito de 𝑛.

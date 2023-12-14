from math import gcd, lcm

# 11. Escribir un programa que calcule el mínimo común múltiplo (mcm) de dos números
# enteros, de dos formas diferentes:
# a) Mediante la función lcm del módulo math.

num1 = 9
num2 = 7

mcma = lcm(num1, num2)

# b) Aprovechando la siguiente propiedad:
# a · b = 𝑚𝑐𝑑 (a, b) · 𝑚𝑐𝑚(a, b)

num_1 = 9
num_2 = 7

mcmb = (num_1 * num_2) / gcd(num_1, num_2)

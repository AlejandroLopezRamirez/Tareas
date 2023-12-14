# 11. Escribe un programa que calcule la longitud y
# el área de una circunferencia. Para ello, el usuario
# debe introducir el radio (que puede contener decimales).

# Recordemos:
# 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 =2𝜋 ·𝑟𝑎𝑑𝑖𝑜
# ́𝑎𝑟𝑒𝑎 =𝜋 ·𝑟𝑎𝑑𝑖𝑜²
import math
r = float(input('Introduzca el radio de la circumferencia: '))

print('La longitud de la circunferencia es', 2 * math.pi * r, 'y el área es', math.pi * pow(r, 2))

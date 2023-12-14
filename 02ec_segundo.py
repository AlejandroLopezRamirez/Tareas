from math import sqrt

#Valores
a = 2.0
b = 23.0
c = 4.0

#Datos intermedios
disc = b ** 2 - 4 * a * c
denom = 2 * a

#Salidas
x1 = (-b + (sqrt(disc)) / denom) if disc >= 0 else "ERROR"

x2 = (-b - (sqrt(disc)) / denom) if disc >= 0 else "ERROR"

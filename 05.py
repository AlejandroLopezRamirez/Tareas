from math import sqrt
# 5. Escribir una función que calcule la distancia euclídea entre dos puntos (𝑥1, 𝑦1) y (𝑥2, 𝑦2),
# descrita por la siguiente especificación:

#    Pre : True
#        distancia(𝑥1: float, 𝑦1: float, 𝑥2: float, 𝑦2: float) -> float

#    Post : distancia (𝑥1, 𝑦1, 𝑥2, 𝑦2) =√︁[(𝑥1 − 𝑥2)² + (𝑦1 − 𝑦2)²]

distancia = lambda a, b, x, y: sqrt(pow((a - b), 2) + pow((x - y), 2))

#Dar un ejemplo de uso.

#3. Escribir una función que implemente la siguiente especificación:

#    Pre : len(𝑐) ≥ 0
#    es_vocal(𝑐: str) -> bool
#    Post : es_vocal(𝑐) = 𝑐 es una vocal, acentuada o no

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

es_vocal = lambda c: c.translate(c.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")) in vocales

# Dar un ejemplo de uso.

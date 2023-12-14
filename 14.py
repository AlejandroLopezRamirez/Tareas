# 14. La función enesimo tiene la siguiente especificación:

# | Pre :   t ≠() ∧ 0 ≤ 𝑛 < len(𝑡)
# {         enesimo(𝑛:int, 𝑡:tuple)
# | Post :  enesimo(𝑛, 𝑡) =el n-ésimo elemento de t


# Escribir una función recursiva que satisfaga dicha especificación.

enesimo = lambda n, t: t[0] if n == 0 else enesimo(n - 1, t[1:])

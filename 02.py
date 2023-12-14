# 2. La función potencia tiene la siguiente especificación:

#         | Pre:    𝑏 ≥ 0
# 𝑓 (𝑛) = {         potencia(𝑎:int, 𝑏:int) -> int
#         | Post:   potencia(𝑎, 𝑏) = 𝑎ᵇ

# a) Implementar la función de forma no recursiva.

potencia = pow

# b) Implementar la función de forma recursiva.

rec_potencia = lambda a, b: 1 if b == 0 else a * rec_potencia(a, (b - 1))

# fr (2,3) = 2 * fr(2, 2)
# fr (2,3) = 2 * 2 fr(2, 1)
# fr (2,3) = 2 * 2 * 2 * 1 --> 8

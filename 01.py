#1. Dada la siguiente función matemática:

#         | 0               si 𝑛 =0
# 𝑓 (𝑛) = {
#         | 1 +2 ·𝑓 (𝑛 −1)  si 𝑛 >0

# calcular el valor de 𝑓 (3)

f = lambda n: 0 if n == 0 else 1 + 2 * f(n - 1)

#f(3) = 1 + 2 * 1 + 2 * 1 + 2 --> 7

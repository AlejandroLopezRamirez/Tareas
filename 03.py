# 3. La función repite tiene la siguiente especificación:

#         | Pre:    𝑛 ≥ 0
# 𝑓 (𝑛) = {         repite(𝑠: str, 𝑛: int) -> str
#         | Post:   repite(s, n) = s * n

# Implementar la función de forma recursiva.


f = lambda s, n : "" if n == 0 else s + f(s, n - 1)

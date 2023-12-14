# 16. La función palindromo tiene la siguiente especificación:

# | Pre :   True
# {         palindromo(t:tuple) -> bool
# |                      | True     si t es un palindromo (se lee igual en ambos sentidos)
# | Post :  palindromo(t){
# |                      | False    en caso contrario

# Por ejemplo: palindromo((1, 2, 3, 4, 3, 2, 1)) == True.

# Escribir una función recursiva que satisfaga dicha especificación.

invertir = lambda t: () if t == () else invertir(t[1:]) + (t[0],)

palindromo = lambda t: t == invertir(t)

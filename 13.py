# 13. Escribir un programa que diga si dos cadenas son iguales sin tener en cuenta las
# mayúsculas y minúsculas. Por ejemplo, el programa debería decir que las cadenas
# "Hola" y "hoLa" son iguales.

str1 = "Hola"
str2 = "hoLa"

str1_cap = str1.capitalize()
str2_cap = str2.capitalize()

igual = "Las dos cadenas son iguales" if str1_cap == str2_cap else "Las cadenas son distintas"

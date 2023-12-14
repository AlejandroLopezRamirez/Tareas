# 15. Escribir un programa que diga si una cadena es un palíndromo.
# Un palíndromo es una cadena que se lee igual de izquierda a derecha que al revés. Por
# ejemplo: «Dábale arroz a la zorra el abad».
# Deben ignorarse las tildes, las mayúsculas y los espacios en blanco. Para ello, hacer uso
# de las soluciones encontradas en los ejercicios anteriores.

pal = "Dábale arroz a la zorra el abad"

mapal = pal.maketrans("áéíóú", "aeiou")

sin_pal = pal.translate(mapal)                    #Aquí se han eliminado todas las tildes

minus_pal = sin_pal.lower()                       #Aquí se han eliminado las mayúsculas

spalce = minus_pal.replace(" ", "")               #Aquí se han eliminado los espacios

resultado = spalce [::-1] == spalce

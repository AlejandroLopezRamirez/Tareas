# 14. Usando el método maketrans definido sobre las cadenas, escribir un programa que
# sustituya en una cadena las vocales acentuadas por sus correspondientes sin acentuar.
# Por ejemplo, si la entrada es la cadena "¡Ramón! ¡Cuánto tiempo! ¿Cómo estás?", la
# salida deberá ser "¡Ramon! ¡Cuanto tiempo! ¿Como estas?".

tildes = "¡Ramón! ¡Cuánto tiempo! ¿Cómo estás?"

mapa = tildes.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")   #Genera un mapa de lo que quiero sustituir

sin_tildes = tildes.translate(mapa)        #Aplica el mapa generado anteriormente

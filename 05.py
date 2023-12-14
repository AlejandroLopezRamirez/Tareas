"""
Los medicos forenses utilizan la longitud de los huesos para
determinar la altura de una persona, cuando la persona estaba
viva.

Por ejemplo, para los varones:

altura(en cm) = 69.089 + 2.232 * longitud de la tibia

Para las mujeres, el valor es el siguiente:

altura(en cm) = 61.412 + 2.317 * longitud de la tibia

A partir de los 30 años (inclusive), la altura de una persona decrece
a una tasa de 0.06 cm por año.

Escribir un programa que, dados los valores de la longitud de
la tibia, el sexo y la edad del paciente, nos calcule la
altura aproximada.
"""

#Datos de entrada:
LONG_TIBIA = 30.4
SEXO = "V"
EDAD = 45

#Dato intermedio
APROX = (69.089 + 2.232 * LONG_TIBIA) if SEXO == "V" else \
        (61.412 + 2.317 * LONG_TIBIA)

#Datos de salida:
ALTURA = APROX - (0.06 * (EDAD - 29)) if EDAD >= 30 else APROX

# 10. Escribir un programa que reciba tres datos de entrada y que los ordene de menor a
# mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.

d_1 = 50
d_2 = 80
d_3 = 45

#Ordenar los 3 números usando variables auxiliares
primero = d_1 if d_1 >= d_2 and d_1 >= d_3 else d_2 if d_2 >= d_1 and d_2 >= d_3 else d_3
ultimo = d_1 if d_1 <= d_2 and d_1 <= d_3 else d_2 if d_2 <= d_1 and d_2 <= d_3 else d_3
segundo = d_1 if (primero == d_2 or primero == d_3) and (ultimo == d_2 or ultimo == d_3) else \
          d_2 if (primero == d_1 or primero == d_3) and (ultimo == d_1 or ultimo == d_3) else d_3

orden_3 = str(primero) + " " + str(segundo) + " " + str(ultimo)

#Division segura: Le pasas dos parámetros y lo divide si el resto es igual a 0, si no no

division_segura=lambda x, y: x / y if y!=0 else "No da exacto"

#Maximo de 3 números
maximo3=lambda x, y, z: x if x >= y and x >= z else y if y > z else z

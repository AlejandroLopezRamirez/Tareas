# 4. Escribir una función calculadora a la que se le pasan dos números reales y qué
# operación se desea realizar con ellos. Las operaciones disponibles son: sumar, restar,
# multiplicar o dividir. Éstas se especifican mediante un carácter: '+', '-', '*' o '/',
# respectivamente. La función devolverá el resultado de la operación en forma de número
# real.

calculadora = lambda x, y, z: x + y if z == "+" \
              else x - y if z == "-" \
              else x * y if z == "*" \
              else x / y

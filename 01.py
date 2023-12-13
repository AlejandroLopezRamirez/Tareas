'''
Escribir en Python una función pura llamada intercambiar(persona)
que reciba una cadena con el nombre (que puede ser compuesto) y los
apellidos (que también pueden ser compuestos) de una persona,
en ese orden y separados por exactamente dos espacios en blanco,
y los devuelva en una cadena poniendo primero los apellidos y
después el nombre, separados por «,␣» (una coma y un espacio).

Si la cadena recibida no tiene la forma requerida,
debe devolverla tal cual sin modificar.

En la cadena recibida no puede haber números ni otros
signos de puntuación salvo los espacios en blanco.
'''

intercambiar = lambda s: s.split('  ')[1:][0] + ', ' + s.split('  ')[0] if s.find('  ') != -1 else s

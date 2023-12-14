def salir():
    '''Un programa que determina si el usuario
    puede salir o no a la calle'''

    lluvia = 'no' == input('¿Está lloviendo?').lower()
    tarea = 'si' == input('¿Acabaste tus tareas?').lower()
    biblioteca = 'si' == input('¿Debes ir a la biblioteca?').lower()

    return 'Si' if biblioteca or (tarea and lluvia) else 'No'


salir()

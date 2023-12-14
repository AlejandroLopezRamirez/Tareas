perdida = 0
def calculate_losses (robado):
    '''¡Acabas de regresar a casa y descubres que han robado tu mansión! Dado un diccionario de
    los artículos robados, devolver el monto total del robo (número). Si no se robó nada, devolver
    la cadena "Lucky you!".'''
    return 'Lucky you!' if robado == {} else sum(robado.values())

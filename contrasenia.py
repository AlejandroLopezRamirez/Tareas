import password

def useradd(x):
    '''Para crear usuarios'''
    ctrs = input('Añada una contraseña para ', x, ' : ')
    password.credencial(x,ctrs)

#def chpasswd(x):
#    (x(1)) = input('Introduzca la nueva contraseña: ')

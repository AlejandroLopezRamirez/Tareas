class Usuario:
    """Usuario y sus claves"""
    def __init__(self, usuario, contrasenia, dni):
        '''Inicializar'''
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.__dni = dni

    def __eq__(self, objeto_importado):
        if type(self) != type(objeto_importado):
            return NotImplemented
        return self.__dni == objeto_importado.get_dni()

    def __hash__(self):
        return hash(self.__dni)

    def __repr__(self):
        '''Representa a la clase'''
        return f'Usuario({repr(self.__usuario)}, {self.__contrasenia}, {repr(self.__dni)})'

    def get_user(self):
        '''Devuelve usuario'''
        return f'El usuario es: {self.__usuario}'

    def get_dni(self):
        return self.__dni

    def set_user(self, contrasenia, usuario_nuevo):
        '''Cambia el usuario'''
        if self.__contrasenia == contrasenia:
            self.__usuario = usuario_nuevo
            return 'Cambio de usuario exitoso'
        return 'Contraseña inválida'

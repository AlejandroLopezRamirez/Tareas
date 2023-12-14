class Credenciales:

    def __init__(self, usuario, clave):
        """Crea un usuario con contraseña"""
        self.__usuario = usuario
        self.__clave = clave

    def consultar(self):
        """Devuelve el usuario"""
        return self.__usuario

    def cambiar_usuario(self, usuario, clave):
        """Cambia al usuario si la contraseña es correcta"""
        if clave == self.__clave:
            self.__usuario = usuario
            print("Usario cambiado")
            return 0
        print("Error en la contraseña")
        return 1

    def cambiar_clave(self, newclave, clave):
        """Cambia al usuario si la contraseña es correcta"""
        if clave == self.__clave:
            self.__clave = newclave
            print("clave cambiada")
            return 0
        print("Error en la contraseña")
        return 1

user1 = Credenciales("jaime", 1234)

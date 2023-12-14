class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)

    def set_dni(self, dni):
        self.__dni = dni

    def get_dni(self):
        return self.__dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_apellidos(self):
        return self.__apellidos

    def __eq__(self, otro) -> bool:
        return self.get_dni() == otro.get__dni()

    def __hash__(self) -> int:
        return hash(self.get_dni())

class Cuenta:
    __numero = 0

    def __init__(self, titular):
        self.__set_numero()
        self.set_titular(titular)
        self.__movimientos = []
        self.__saldo = 0

    def __set_numero(self):
        Cuenta.__numero +=1
        self.__numero = Cuenta.__numero

    def get_numero(self):
        return self.__numero

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def set_movimientos(self, movimientos):
        self.__movimientos = movimientos

    def get_movimientos(self):
        return self.__movimientos

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def __repr__(self):
        print('Nº Cuenta: ', self.get_numero())
        print('Titular: ', self.get_titular())
        print('Movimientos: ', self.get_movimientos())
        return 'Saldo: ' + str(self.get_saldo())

    def __eq__(self, otro):
        return self.get_numero() == otro.get_numero()

    def __hash__(self) -> int:
        return hash(self.get_numero())

class Movimientos:
    def __init__(self, concepto, cantidad):
        self.set_concepto(concepto)
        self.set_cantidad(cantidad)

    def set_concepto(self, concepto):
        if concepto in ("Retirar", "Ingresar"):
            self.__concepto = concepto
        raise ValueError('Concepto erróneo.')

    def get_concepto(self):
        return self.__concepto

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    '''def operacion(self, concepto, cantidad, cuenta):
        if concepto == 'Retirar' and cantidad >= cuenta.get_saldo():
            raise ValueError('No hay saldo suficiente.')
        elif concepto == 'Retirar':
            cuenta.set_saldo(cuenta.get_saldo() + )'''

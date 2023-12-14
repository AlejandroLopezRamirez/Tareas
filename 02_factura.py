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

    def nombre_completo(self):
        return self.get_nombre() + ' ' + self.get_apellidos()

class Articulo:
    def __init__(self, codigo, denominacion, precio):
        self.set_codigo(codigo)
        self.set_denominacion(denominacion)
        self.set_precio(precio)

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_codigo(self):
        return self.__codigo

    def set_denominacion(self, denominacion):
        self.__denominacion = denominacion

    def get_denominacion(self):
        return self.__denominacion

    def set_precio(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def __repr__(self):
        return self.get_denominacion()

class Factura:
    def __init__(self, numero, cliente):
        self.set_numero(numero)
        self.set_cliente(cliente)
        self.set_lineas()

    def set_numero(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_cliente(self, cliente):
        self.__cliente = cliente.nombre_completo()

    def get_cliente(self):
        return self.__cliente

    def set_lineas(self):
        self.__lineas = {}

    def get_lineas(self):
        return self.__lineas

    def anadir(self, articulo, cantidad):
        self.__lineas.update({articulo:cantidad})

    def eliminar(self, articulo):
        del self.get_lineas()[articulo]

    def total(self):
        total=0
        for x, y in self.get_lineas().items():
            total += (x.get_precio() * y)
        return total

    def ver(self):
        print(self.get_numero())
        print(self.get_lineas())
        print(self.total(),'€')


c1=Cliente('49494949R', 'Jaime', 'Garcia Pedrote')

a1=Articulo('01', 'Televisión', 399)
a2=Articulo('02', 'GPU', 239)

f1=Factura('01', c1)

f1.anadir(a1, 2)
f1.anadir(a2, 1)

f1.ver()

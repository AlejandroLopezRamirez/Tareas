import datetime

class Lector:
    __numero = 0

    def __init__(self, nombre, apellidos):
        self.__set_numero()
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.__moroso = False

    def __set_numero(self):
        Lector.__numero += 1
        self.__numero = Lector.__numero

    def get_numero(self):
        return self.__numero

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_apellidos(self,apellidos):
        self.__apellidos = apellidos

    def get_apellidos(self):
        return self.__apellidos

    def set_moroso(self,moroso):
        self.__moroso = moroso

    def get_moroso(self):
        return self.__moroso

    def nombre_completo(self):
        return self.get_nombre() + ' ' + self.get_apellidos()


class Libro:
    __numero = 0

    def __init__(self, titulo, autor, editorial):
        self.__set_codigo()
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_editorial(editorial)
        self.set_prestado(False)

    def __set_codigo(self):
        Libro.__numero += 1
        self.__codigo = Libro.__numero

    def get_codigo(self):
        return self.__codigo

    def set_titulo(self,titulo):
        self.__titulo = titulo

    def get_titulo(self):
        return self.__titulo

    def set_autor(self,autor):
        self.__autor = autor

    def get_autor(self):
        return self.__autor

    def set_editorial(self,editorial):
        self.__editorial = editorial

    def get_editorial(self):
        return self.__editorial

    def set_prestado(self,prestado):
        self.__prestado = prestado

    def get_prestado(self):
        return self.__prestado


class Prestamo:
    def __init__(self, lector, libro):
        self.__set_lector(lector)
        self.__set_libro(libro)
        self.__set_fecha_prestamo()
        self.__set_fecha_devolucion(None)

    def __set_lector(self,lector):
        self.__lector = lector

    def get_lector(self):
        return self.__lector.nombre_completo()

    def __set_libro(self,libro):
        if libro.get_prestado() is True:
            raise ValueError('Este libro ya ha sido prestado')
        self.__libro = libro
        libro.set_prestado(True)
        return print('Préstamo realizado')

    def get_libro(self):
        return self.__libro.get_nombre()

    def __set_fecha_prestamo(self):
        self.__fecha_prestamo = datetime.datetime.now()

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def __set_fecha_devolucion(self,fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def devuelto(self):
        self.__set_fecha_devolucion(datetime.datetime.now())
        self.__libro.set_prestado(False)
        expirado = self.__fecha_prestamo + datetime.timedelta(15)
        if self.get_fecha_devolucion() > expirado:
            self.__lector.set_moroso(True)

'''le1 = Lector('Ana', 'García')
le2 = Lector('Roberto', 'Sánchez')

li1 = Libro('El camino', 'Miguel Delibes', 'Misco')
li2 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Misco')
li3 = Libro('Rayuela', 'Julio Cortázar', 'Misco')

p1 = Prestamo(le1, li1)
p2 = Prestamo(le2, li1)
p1.devuelto()'''

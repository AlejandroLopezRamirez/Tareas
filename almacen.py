class Articulo:
    def __init__(self, nombre):
        self.set_nombre(nombre)
        self.set_cantidad()

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_cantidad(self):
        self.__cantidad = 0

    def get_cantidad(self):
        return self.__cantidad

    def __repr__(self):
        return f'Articulo({(self.get_nombre())!r}, {(self.get_cantidad())!r})'

    def __str__(self) -> str:
        return f'Nombre del artículo: {(self.get_nombre())!r}, Cantidad del artículo: {(self.get_cantidad())!r}'

class Gestion_articulo:
    lista = {}
    def __init__(self):
        pass

    @staticmethod
    def alta_articulo(nombre):
        if nombre in Gestion_articulo.lista:
            raise ValueError('Artículo ya dado de alta')
        Articulo(nombre)
        Gestion_articulo.lista.update({nombre:0})

    @staticmethod
    def agregar_cantidad_articulo(nombre, cantidad):
        if nombre not in Gestion_articulo.lista:
            raise ValueError('Artículo no dado de alta')
        Gestion_articulo.lista[nombre] = cantidad

    @staticmethod
    def imprimir_articulos():
        total=0
        for x,y in Gestion_articulo.lista.items():
            print('---------------------------------')
            print (x + ':', y, '[uds]')
            total += 1
        print('Total de artículos dados de alta:', total)
        print('---------------------------------')


class Albaran:
    __num = 0

    def __init__(self,id_albaran, articulo, cantidad):
        self.__set_num_entrada()
        self.set_id_albaran(id_albaran)
        self.set_articulo(articulo)
        self.set_cantidad(cantidad, articulo)

    def __set_num_entrada(self):
        Albaran.__num += 1
        self.__num_entrada = Albaran.__num

    def get_num_entrada(self):
        return self.__num_entrada

    def set_id_albaran(self, id_albaran):
        self.__id_albaran = id_albaran

    def get_id_albaran(self):
        return self.__id_albaran

    def set_articulo(self, articulo):
        Gestion_articulo.alta_articulo(articulo)
        self.__articulo = articulo

    def get_articulo(self):
        return self.__articulo

    def set_cantidad(self, cantidad, nombre):
        Gestion_articulo.agregar_cantidad_articulo(nombre,cantidad)
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

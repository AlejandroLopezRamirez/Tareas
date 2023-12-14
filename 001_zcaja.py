class Electrodomestico:
    def __init__(self, consumo, fabricante, ffabricacion) -> None:
        self.set_consumo(consumo)
        self.set_fabricante(fabricante)
        self.set_ffabricacion(ffabricacion)

    def set_consumo(self, consumo):
        self.consumo = consumo

    def get_consumo(self):
        return self.consumo

    def set_fabricante(self, fabricante):
        self.fabricante = fabricante

    def get_fabricante(self):
        return self.fabricante

    def set_ffabricacion(self, ffabricacion):
        self.ffabricacion = ffabricacion

    def get_ffabricacion(self):
        return self.ffabricacion

    def __repr__(self) -> str:
        return f'Electrodomestico({self.get_consumo()}, {self.get_fabricante()!r}, {self.get_ffabricacion()!r})'

    def __str__(self) -> str:
        return f'Consumo: {self.get_consumo()}, Fabricante: {self.get_fabricante()!r}, Fecha de Fábrica: {self.get_ffabricacion()!r}'

class Nevera(Electrodomestico):
    def __init__(self, consumo, fabricante, ffabricacion, capacidad) -> None:
        super().__init__(consumo, fabricante, ffabricacion)
        self.set_capacidad(capacidad)

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def get_capacidad(self):
        return self.capacidad

class Calc:
    def __init__(self, a,b):
        self.set_a(a)
        self.set_b(b)

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    def get_b(self):
        return self.__b

    def set_b(self, b):
        self.__b = b

    def sumar(self):
        return self.get_a() + self.get_b()

    def restar(self):
        return self.get_a() - self.get_b()

    @staticmethod
    def sumar_e(a,b):
        return a + b

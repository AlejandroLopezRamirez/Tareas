import re
class numero:
    bases = ['decimal', 'binario', 'octal', 'hexadecimal', 'BCD', 'romano']

    def __init__(self, numero, base) -> None:
        self.set_numero(numero, base)
        self.set_base(base)

    def set_numero(self, numero, base):
        self.numero = numero

    def get_numero(self):
        return self.numero

    def set_base(self, base):
        if base in numero.bases:
            self.base = base
            return "Base aceptada"
        raise ValueError('Base no aceptada')

    def get_base(self):
        return self.base

    def __str__(self) -> str:
        return f'Número --> {self.get_numero()}  Base --> {self.get_base()}'

    def go_decimal(self):
        if self.get_base() == 'decimal':
            return self.get_numero()

        if self.get_base() == 'binario':
            num=str(self.get_numero())
            return int(num, 2)

        if self.get_base() == 'octal':
            num=str(self.get_numero())
            return int(num, 8)

        if self.get_base() == 'hexadecimal':
            num=str(self.get_numero())
            return int(num, 16)

        if self.get_base() == 'BCD':
            pass

        if self.get_base() == 'romano':
            roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            num = self.get_numero()[::-1]
            acc = 0
            ant = 0
            for x in num:
                if ant >= roman[x] :
                    acc = acc - roman[x]
                else:
                    acc = acc + roman[x]
                ant = roman [x]
            return acc

    @staticmethod
    def check_bin(numero):
        return len(re.findall("[0-9A-F]", str(numero))) == len(str(numero))

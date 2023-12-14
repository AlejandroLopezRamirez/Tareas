class hora:
    def __init__(self, hora, minutos) -> None:
        self.set_hora(hora)
        self.set_minutos(minutos)

    def set_hora(self, hora):
        if hora <= 23:
            self.hora = hora
        return hora <= 23

    def get_hora(self):
        return self.hora

    def set_minutos(self, minutos):
        if minutos <= 59:
            self.minutos = minutos
        return minutos <= 59

    def get_minutos(self):
        return self.minutos

    def inc(self):
        if self.set_minutos(self.get_minutos() + 1):
            return "Hora actualizada"
        self.set_minutos(0)
        if self.set_hora(self.get_hora() + 1):
            return "Hora actualizada"
        self.set_hora(0)
        return "Hora actualizada"

    def __str__(self) -> str:
        return f'{self.get_hora():>02}:{self.get_minutos():>02}'

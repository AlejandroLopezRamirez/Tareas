class personaje:

    def __init__(self, fuerza, defensa, vida):
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    def stats(self):
        print("Fuerza:", self.fuerza)

morgan = personaje(2, 20, 100)
morgan.stats()

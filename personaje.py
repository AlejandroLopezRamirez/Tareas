class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        """Crea un personaje"""
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        """Enseña los atributos del personaje"""
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        """Aumenta las estadísticas del personaje"""
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        """Comprueba si el personaje está vivo"""
        return self.vida > 0

    def morir(self):
        "Pone la vida del perosnaje a 0 y anuncia su muerte"
        self.vida = 0
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        """Calcula el daño ralizado en un ataque"""
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        """Modifica la vida del enemigo con el daño calculado"""
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, "ha realizado", damage, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

mi_personaje = Personaje("Mizu", 10, 1, 5, 100)
mi_enemigo = Personaje("Villano", 8, 5, 3, 5)

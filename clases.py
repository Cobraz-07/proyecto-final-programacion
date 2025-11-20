
class Personaje:
    def __init__(self, nombre, jugable):
        self.nombre = nombre
        self.jugable = jugable

mario = Personaje("Mario", True)

luigi = Personaje("Luigi", True)

boss = Personaje("Boss", False)

class Cinta:
    def __init__(self, posicion, numerodif):
        self.posicion = posicion
        self.numero = numerodif

cinta0 = Cinta("Cinta0")

cintasImpares = Cinta("CintasImpares")

cintasPares = Cinta("CintasPares")


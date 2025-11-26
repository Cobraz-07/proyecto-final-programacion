import pyxel


class Camion:
    def __init__(self):
        self.pos_x = 2
        self.pos_y = 54
        self.paquetes = 0

    def draw(self):
        u = self.paquetes * 32
        pyxel.blt(self.pos_x, self.pos_y, 0, u, 48, 32, 32, 1)

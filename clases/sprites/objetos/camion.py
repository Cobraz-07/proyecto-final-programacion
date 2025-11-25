import pyxel


class Camion:
    def __init__(self):
        self.pos_x = 2
        self.pos_y = 54

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, 0, 48, 32, 32, 1)

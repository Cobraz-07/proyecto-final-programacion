import pyxel


class Mario:
    def __init__(self):
        self.posicion_y = 100

    def draw(self):
        pyxel.blt(200, self.posicion_y, 0, 16, 0, 16, 16, 0)

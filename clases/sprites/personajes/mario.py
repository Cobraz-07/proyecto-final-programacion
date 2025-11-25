import pyxel


class Mario:

    POSICION_1_Y = 109
    POSICION_1_X = 182
    POSICION_2_Y = 79
    POSICION_2_X = 182
    POSICION_3_Y = 45
    POSICION_3_X = 182

    def __init__(self):
        self.posicion_y = self.POSICION_1_Y
        self.posicion_x = self.POSICION_1_X

    def draw(self):
        pyxel.blt(self.posicion_x, self.posicion_y, 0, 32, 0, 16, 16, 0)

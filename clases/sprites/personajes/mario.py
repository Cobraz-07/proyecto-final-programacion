import pyxel


class Mario:

    def __init__(self):
        self.posicion = 1
        self.posicion_1_y = 109
        self.posicion_2_y = 79
        self.posicion_3_y = 45
        self.posicion_x = 182
        self.paquetePorDerecha = False
        self.timer_animacion = 0

    def draw(self):

        if self.timer_animacion > 0:
            pyxel.blt(self.posicion_x, self.posicion_1_y, 0, 0, 32, 16, 16, 0)

        else:
            if self.posicion == 1:
                pyxel.blt(self.posicion_x, self.posicion_1_y, 0, 32, 0, 16, 16, 0)
            elif self.posicion == 2:
                pyxel.blt(self.posicion_x, self.posicion_2_y, 0, 0, 32, 16, 16, 0)
            elif self.posicion == 3:
                pyxel.blt(self.posicion_x, self.posicion_3_y, 0, 0, 32, 16, 16, 0)

    def interactuar(self):
        self.timer_animacion = 10

    def move(self):
        if self.timer_animacion > 0:
            self.timer_animacion -= 1
            return

        if pyxel.btnp(pyxel.KEY_UP) and self.posicion < 3:
            self.posicion += 1

        if pyxel.btnp(pyxel.KEY_DOWN) and self.posicion > 1:
            self.posicion -= 1

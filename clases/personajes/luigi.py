import pyxel


class Luigi:

    def __init__(self):
        self.posicion = 1
        self.posicion_1_y = 96
        self.posicion_2_y = 62
        self.posicion_3_y = 28
        self.posicion_x = 55
        self.paquetePorDerecha = False
        self.timer_animacion = 0

    def draw(self):
        if self.timer_animacion > 0:
            pyxel.blt(self.posicion_x, self.posicion_3_y, 0, 32, 32, 16, 16, 0)

        else:
            if self.posicion == 1:
                pyxel.blt(self.posicion_x, self.posicion_1_y, 0, 16, 0, 16, 16, 0)
            elif self.posicion == 2:
                pyxel.blt(self.posicion_x, self.posicion_2_y, 0, 16, 0, 16, 16, 0)
            elif self.posicion == 3:
                pyxel.blt(self.posicion_x, self.posicion_3_y, 0, 16, 0, 16, 16, 0)

    def drawVictoria(self, x, y):
        if (pyxel.frame_count // 10) % 2 == 0:
            ancho = 16
        else:
            ancho = -16
        pyxel.blt(x, y, 0, 16, 0, ancho, 16, 0)

    def interactuar(self):
        self.timer_animacion = 10

    def move(self):
        if self.timer_animacion > 0:
            self.timer_animacion -= 1
            return

        if pyxel.btnp(pyxel.KEY_W) and self.posicion < 3:
            self.posicion += 1
        if pyxel.btnp(pyxel.KEY_S) and self.posicion > 1:
            self.posicion -= 1

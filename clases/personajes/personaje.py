import pyxel


class Personaje:
    def __init__(self, x, y_positions, teclas, sprite_victoria_u):
        self.posicion = 1
        self.timer_animacion = 0

        self.posicion_x = x
        self.y_positions = y_positions
        self.key_up = teclas[0]
        self.key_down = teclas[1]
        self.sprite_victoria_u = sprite_victoria_u

    def move(self):
        if self.timer_animacion > 0:
            self.timer_animacion -= 1
            return

        if pyxel.btnp(self.key_up) and self.posicion < 3:
            self.posicion += 1

        if pyxel.btnp(self.key_down) and self.posicion > 1:
            self.posicion -= 1

    def interactuar(self):
        self.timer_animacion = 10

    def drawVictoria(self, x, y):
        if (pyxel.frame_count // 10) % 2 == 0:
            ancho = 16
        else:
            ancho = -16

        pyxel.blt(x, y, 0, self.sprite_victoria_u, 0, ancho, 16, 0)

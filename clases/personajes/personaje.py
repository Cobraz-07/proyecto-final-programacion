import pyxel


class Personaje:
    def __init__(self, x, y_positions, teclas, sprite_victoria_u):
        self._posicion = 1  # Posición (en relación a las alturas)
        self.timer_animacion = 0

        self.posicion_x = x
        self.y_positions = y_positions  # Lista de alturas posibles
        self.key_up = teclas[0]
        self.key_down = teclas[1]
        self.sprite_victoria_u = sprite_victoria_u

    # Propiedad para que desde fuera puedan leer 'mario.posicion'
    @property
    def posicion(self):
        return self._posicion

    def move(self):
        # Si está en animación, bloquear movimiento
        if self.timer_animacion > 0:
            self.timer_animacion -= 1
            return

        # Movimiento arriba/abajo entre los pisos definidos
        if pyxel.btnp(self.key_up) and self.posicion < 3:
            self._posicion += 1

        if pyxel.btnp(self.key_down) and self.posicion > 1:
            self._posicion -= 1

    def interactuar(self):
        # Inicia pequeña animación al pasar paquete de derecha a izquierda
        self.timer_animacion = 10

    def drawVictoria(self, x, y):
        # Animación de baile en pantalla final
        if (pyxel.frame_count // 10) % 2 == 0:
            ancho = 16
        else:
            ancho = -16

        pyxel.blt(x, y, 0, self.sprite_victoria_u, 0, ancho, 16, 0)

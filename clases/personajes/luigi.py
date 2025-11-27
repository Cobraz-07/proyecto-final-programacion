import pyxel
from .personaje import Personaje


class Luigi(Personaje):
    def __init__(self):
        # Configurar posición inicial, teclas (W/S) y sprites de Luigi
        super().__init__(
            x=55,
            y_positions=(96, 62, 28),
            teclas=(pyxel.KEY_W, pyxel.KEY_S),
            sprite_victoria_u=16,
        )

    def draw(self):
        # Dibujar sprite de interacción
        if self.timer_animacion > 0:
            pyxel.blt(self.posicion_x, self.y_positions[2], 0, 32, 32, 16, 16, 0)
            return

        # Dibujar sprite normal
        y_actual = self.y_positions[self.posicion - 1]
        pyxel.blt(self.posicion_x, y_actual, 0, 16, 0, 16, 16, 0)

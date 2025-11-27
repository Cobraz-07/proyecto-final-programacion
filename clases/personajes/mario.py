import pyxel
from .personaje import Personaje


class Mario(Personaje):
    def __init__(self):
        super().__init__(
            x=182,
            y_positions=(109, 79, 45),
            teclas=(pyxel.KEY_UP, pyxel.KEY_DOWN),
            sprite_victoria_u=32,
        )

    def draw(self):
        if self.timer_animacion > 0:
            pyxel.blt(self.posicion_x, self.y_positions[0], 0, 0, 32, 16, 16, 0)
            return

        y_actual = self.y_positions[self.posicion - 1]

        if self.posicion == 1:
            u, v = 32, 0
        else:
            u, v = 0, 32

        pyxel.blt(self.posicion_x, y_actual, 0, u, v, 16, 16, 0)

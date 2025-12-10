import pyxel


class Personaje:
    def __init__(self, x, y_positions, teclas):
        # Altura actual relativa (1, 2 o 3)
        self._posicion = 1
        self.timer_animacion = 0
        self.posicion_x = x
        self.y_positions = y_positions
        self.key_up = teclas[0]
        self.key_down = teclas[1]

    @property
    def posicion(self):
        # Getter para acceder a la altura actual
        return self._posicion

    def move(self):
        # Bloquea controles si hay una animación activa
        if self.timer_animacion > 0:
            self.timer_animacion -= 1
            return

        # Sube de nivel si no está en el tope
        if pyxel.btnp(self.key_up) and self.posicion < 3:
            self._posicion += 1

        # Baja de nivel si no está en el suelo
        if pyxel.btnp(self.key_down) and self.posicion > 1:
            self._posicion -= 1

    def interactuar(self):
        # Activa breve animación al manipular un paquete
        self.timer_animacion = 10

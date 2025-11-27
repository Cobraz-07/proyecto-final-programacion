import pyxel


class Jefe:
    def __init__(self):
        self.regañando = False
        self.doble = False  # Si aparecen dos jefes (entre niveles)
        self.timer = 0
        self.duracion = 60  # Duración del regaño

        # Posiciones posibles
        self.pos_x = 0
        self.pos_y = 0
        self.posicion_1_x = 11
        self.posicion_1_y = 119
        self.posicion_2_x = 227
        self.posicion_2_y = 79

        self.ancho = 16

    def aparecer(self, x_paquete):
        # Configura al jefe para regañar en el lado donde cayó el paquete
        self.regañando = True
        self.doble = False
        self.timer = self.duracion

        # Determinar lado izquierdo o derecho
        if x_paquete < 128:
            self.pos_x = self.posicion_1_x
            self.pos_y = self.posicion_1_y
            self.ancho = -16  # Invertir sprite
        else:
            self.pos_x = self.posicion_2_x
            self.pos_y = self.posicion_2_y
            self.ancho = 16

    def aparecerDoble(self):
        # Aparecen dos jefes (evento especial al completar carga)
        self.regañando = True
        self.doble = True
        self.timer = self.duracion

    def update(self):
        # Temporizador de visualización
        if self.regañando:
            self.timer -= 1
            if self.timer <= 0:
                self.regañando = False
                self.doble = False

    def draw(self):
        if self.regañando:
            if self.doble:
                # Dibujar en ambos lados
                pyxel.blt(self.posicion_1_x, self.posicion_1_y, 0, 0, 16, -16, 16, 0)
                pyxel.blt(self.posicion_2_x, self.posicion_2_y, 0, 0, 16, 16, 16, 0)
            else:
                # Dibujar solo en el lado activo
                pyxel.blt(self.pos_x, self.pos_y, 0, 0, 16, self.ancho, 16, 0)

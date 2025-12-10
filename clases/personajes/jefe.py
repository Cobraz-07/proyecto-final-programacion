import pyxel


class Jefe:
    def __init__(self):
        self.regañando = False
        self.doble = False
        self.timer = 0
        self.duracion = 60
        self.pos_x = 0
        self.pos_y = 0

        # Coordenadas fijas para las apariciones
        self.posicion_1_x = 11
        self.posicion_1_y = 119
        self.posicion_2_x = 227
        self.posicion_2_y = 79
        self.ancho = 16

    def aparecer(self, x_paquete):
        # Activa el jefe en el lado donde se cayó el paquete
        self.regañando = True
        self.doble = False
        self.timer = self.duracion

        # Selecciona lado y orientación del sprite
        if x_paquete < 128:
            self.pos_x = self.posicion_1_x
            self.pos_y = self.posicion_1_y
            self.ancho = -16
        else:
            self.pos_x = self.posicion_2_x
            self.pos_y = self.posicion_2_y
            self.ancho = 16

    def aparecerDoble(self):
        # Evento especial: aparecen dos jefes simultáneamente
        self.regañando = True
        self.doble = True
        self.timer = self.duracion

    def update(self):
        # Gestiona el tiempo que el jefe permanece en pantalla
        if self.regañando:
            self.timer -= 1
            if self.timer <= 0:
                self.regañando = False
                self.doble = False

    def draw(self):
        # Dibuja uno o dos jefes según el estado
        if self.regañando:
            if self.doble:
                pyxel.blt(self.posicion_1_x, self.posicion_1_y, 0, 0, 16, -16, 16, 0)
                pyxel.blt(self.posicion_2_x, self.posicion_2_y, 0, 0, 16, 16, 16, 0)
            else:
                pyxel.blt(self.pos_x, self.pos_y, 0, 0, 16, self.ancho, 16, 0)

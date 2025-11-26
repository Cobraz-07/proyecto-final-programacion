import pyxel


class Camion:
    def __init__(self):
        self.x_inicial = 2
        self.pos_x = self.x_inicial
        self.pos_y = 54
        self.paquetes = 0
        self.entregas = 0
        self.fallos = 0
        self.puntos = 0

        self.repartiendo = False
        self.timer_salida = 0
        self.tiempo_espera = 30 * 5

    def update(self):
        if self.repartiendo:
            if self.timer_salida > 0:
                self.timer_salida -= 1

                if self.pos_x > -60:
                    self.pos_x -= 2
            else:
                self.finalizar_reparto()

    def iniciar_reparto(self):
        self.repartiendo = True
        self.timer_salida = self.tiempo_espera

    def finalizar_reparto(self):
        self.entregas += 1
        self.puntos += 10
        self.paquetes = 0
        self.repartiendo = False
        self.pos_x = self.x_inicial

    def draw(self):
        u = self.paquetes * 32

        if self.paquetes >= 8 or self.repartiendo:
            pyxel.blt(self.pos_x, self.pos_y, 0, 0, 80, 32, 32, 1)
        else:
            pyxel.blt(self.pos_x, self.pos_y, 0, u, 48, 32, 32, 1)

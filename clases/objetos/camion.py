import pyxel


class Camion:
    def __init__(self):
        self.x_inicial = 2
        self.pos_x = self.x_inicial
        self.pos_y = 54

        # Control de puntuación y estado de juego
        self._paquetes = 0
        self._entregas = 0
        self._fallos = 0
        self._puntos = 0

        # Control de animación de salida
        self.repartiendo = False
        self.timer_salida = 0
        self.tiempo_espera = 30 * 5

    # Propiedades de solo lectura
    @property
    def puntos(self):
        return self._puntos

    @property
    def entregas(self):
        return self._entregas

    @property
    def fallos(self):
        return self._fallos

    @property
    def paquetes(self):
        return self._paquetes

    def cargar_paquete(self):
        self._paquetes += 1

    def registrar_fallo(self):
        self._fallos += 1

    def sumar_puntos(self, cantidad):
        self._puntos += cantidad

    def update(self):
        # Anima la salida del camión hacia la izquierda
        if self.repartiendo:
            if self.timer_salida > 0:
                self.timer_salida -= 1
                if self.pos_x > -60:
                    self.pos_x -= 2
            else:
                self.finalizar_reparto()

    def iniciar_reparto(self):
        # Comienza secuencia de salida y reproduce sonido
        self.repartiendo = True
        self.timer_salida = self.tiempo_espera
        pyxel.play(2, 2)

    def finalizar_reparto(self):
        # Resetea camión, suma puntos y bonifica vidas cada 3 viajes
        self._entregas += 1
        self.sumar_puntos(10)

        if self._entregas == 3:
            self._entregas = 0
            if self._fallos > 0:
                self._fallos -= 1

        self._paquetes = 0
        self.repartiendo = False
        self.pos_x = self.x_inicial

    def draw(self):
        # Calcula sprite según carga o estado
        u = self.paquetes * 32
        if self.paquetes >= 8 or self.repartiendo:
            pyxel.blt(self.pos_x, self.pos_y, 0, 0, 80, 32, 32, 1)
        else:
            pyxel.blt(self.pos_x, self.pos_y, 0, u, 48, 32, 32, 1)

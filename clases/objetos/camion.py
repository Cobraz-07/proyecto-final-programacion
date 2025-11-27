import pyxel


class Camion:
    def __init__(self):
        self.x_inicial = 2
        self.pos_x = self.x_inicial
        self.pos_y = 54

        # Estadísticas del juego
        self.paquetes = 0  # Paquetes cargados actualmente
        self.entregas = 0  # Viajes completados
        self.fallos = 0
        self.puntos = 0

        self.repartiendo = False
        self.timer_salida = 0
        self.tiempo_espera = 30 * 5  # 5 segundos

    def update(self):
        # Lógica de animación cuando el camión se va
        if self.repartiendo:
            if self.timer_salida > 0:
                self.timer_salida -= 1

                # Movimiento hacia la izquierda
                if self.pos_x > -60:
                    self.pos_x -= 2
            else:
                self.finalizar_reparto()

    def iniciar_reparto(self):
        # Comienza la secuencia de salida
        self.repartiendo = True
        self.timer_salida = self.tiempo_espera

    def finalizar_reparto(self):
        # Reinicia el camión y suma puntos
        self.entregas += 1
        self.puntos += 10

        # Bonificación: limpia un fallo si existe
        if self.fallos > 0:
            self.fallos -= 1

        self.paquetes = 0
        self.repartiendo = False
        self.pos_x = self.x_inicial

    def draw(self):
        # Calcular sprite basado en lo lleno que está el camión
        u = self.paquetes * 32

        if self.paquetes >= 8 or self.repartiendo:
            # Sprite de camión lleno/saliendo
            pyxel.blt(self.pos_x, self.pos_y, 0, 0, 80, 32, 32, 1)
        else:
            # Sprite de carga progresiva
            pyxel.blt(self.pos_x, self.pos_y, 0, u, 48, 32, 32, 1)

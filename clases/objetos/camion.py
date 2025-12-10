import pyxel


class Camion:
    def __init__(self):
        self.x_inicial = 2
        self.pos_x = self.x_inicial
        self.pos_y = 54

        # Estadísticas del juego
        self._paquetes = 0  # Paquetes cargados actualmente
        self._entregas = 0  # Viajes completados
        self._fallos = 0
        self._puntos = 0

        self.repartiendo = False
        self.timer_salida = 0
        self.tiempo_espera = 30 * 5  # 5 segundos

    # --- PROPIEDADES (Getters) para leer los valores ---
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

    # --- MÉTODOS para modificar los valores de forma segura ---
    def cargar_paquete(self):
        self._paquetes += 1

    def registrar_fallo(self):
        self._fallos += 1

    def sumar_puntos(self, cantidad):
        self._puntos += cantidad

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
        pyxel.play(2, 2)

    def finalizar_reparto(self):
        # Reinicia el camión y suma puntos
        self._entregas += 1
        self.sumar_puntos(10)

        # Bonificación: limpia un fallo si existe
        if self._fallos > 0:
            self._fallos -= 1

        self._paquetes = 0
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

import pyxel


class Camion:
    def __init__(self):
        self.x_inicial = 2
        self.pos_x = self.x_inicial
        self.pos_y = 54
        self.paquetes = 0
        self.entregas = 0

        # Variables para la animación de salida
        self.repartiendo = False
        self.timer_salida = 0
        self.tiempo_espera = 30 * 5  # 30 FPS * 5 segundos = 150 frames

    def update(self):
        # Si estamos en modo reparto, gestionamos la animación y el tiempo
        if self.repartiendo:
            if self.timer_salida > 0:
                self.timer_salida -= 1

                # Animación: Mover el camión a la izquierda durante el primer segundo
                if self.pos_x > -60:
                    self.pos_x -= 2
            else:
                # Se acabó el tiempo de espera
                self.finalizar_reparto()

    def iniciar_reparto(self):
        self.repartiendo = True
        self.timer_salida = self.tiempo_espera

    def finalizar_reparto(self):
        self.entregas += 1
        self.paquetes = 0
        self.repartiendo = False
        self.pos_x = self.x_inicial  # Vuelve a su sitio

    def draw(self):
        # Dibujo normal
        u = self.paquetes * 32

        # Si tiene 8 paquetes o está repartiendo, usamos el sprite lleno
        if self.paquetes >= 8 or self.repartiendo:
            # Nota: Asumo que el sprite lleno está en u=0, v=80 según tu código original
            # O ajusta las coordenadas según tu banco de recursos si quieres que se vea humo
            pyxel.blt(self.pos_x, self.pos_y, 0, 0, 80, 32, 32, 1)
        else:
            pyxel.blt(self.pos_x, self.pos_y, 0, u, 48, 32, 32, 1)

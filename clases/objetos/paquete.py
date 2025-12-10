import pyxel


class Paquete:
    def __init__(self, cintas, velocidad, play_cambio_de_altura):
        self.cintas = cintas
        self.indice_cinta = 0
        self.play_cambio_de_altura = play_cambio_de_altura

        # Configuración inicial en la primera cinta
        cinta_actual = self.cintas[self.indice_cinta]
        self.pos_x = 249
        self.pos_y = cinta_actual.y
        self.speed = velocidad

        # Estados del paquete
        self.activo = True
        self.fallado = False
        self.cayendo = False
        self.u = 48
        self.v = 0

    def caer(self, x_destino):
        # Inicia estado de caída libre
        self.pos_x = x_destino
        self.cayendo = True

    def cambiar_altura(self, mario, luigi, camion):
        if self.cayendo:
            return

        cinta_actual = self.cintas[self.indice_cinta]

        # Lógica para la primera cinta (interacción con Mario)
        if self.indice_cinta == 0:
            if 180 < self.pos_x <= 197:
                if mario.posicion == 1:
                    mario.interactuar()
                    self.cambiar_cinta()
                    self.pos_x = 148
                else:
                    self.caer(170)
            return

        # Lógica para cintas hacia la izquierda
        if cinta_actual.mueve_a_izquierda:
            if self.pos_x <= 72:
                req_pos = (self.indice_cinta // 2) + 1
                if luigi.posicion == req_pos:
                    if self.indice_cinta == len(self.cintas) - 1:
                        luigi.interactuar()
                        self.activo = False
                        self.fallado = False
                    else:
                        self.cambiar_cinta()
                        self.pos_x = 82
                        camion.sumar_puntos(1)
                else:
                    self.caer(69)
            return

        # Lógica para cintas hacia la derecha
        if not cinta_actual.mueve_a_izquierda:
            if self.pos_x >= 167:
                req_pos = (self.indice_cinta // 2) + 1
                if mario.posicion == req_pos:
                    self.cambiar_cinta()
                    self.pos_x = 154
                    camion.sumar_puntos(1)
                else:
                    self.caer(170)

    def cambiar_cinta(self):
        # Sube a la siguiente cinta y reproduce sonido
        self.play_cambio_de_altura()
        if self.indice_cinta < len(self.cintas) - 1:
            self.indice_cinta += 1
            self.pos_y = self.cintas[self.indice_cinta].y

    def actualizarSprite(self):
        if self.cayendo:
            return

        # Cambia apariencia según en qué cinta y que lado se encuentre
        idx = self.indice_cinta
        if idx == 0 or idx == 1:
            self.u, self.v = (48, 0) if self.pos_x >= 118 else (48, 16)
        elif idx == 2:
            self.u, self.v = (48, 16) if self.pos_x < 118 else (48, 32)
        elif idx == 3:
            self.u, self.v = (48, 32) if self.pos_x >= 118 else (64, 0)
        elif idx == 4:
            self.u, self.v = (64, 0) if self.pos_x < 118 else (64, 16)
        else:
            self.u, self.v = (64, 32) if self.pos_x <= 118 else (64, 16)

    def move(self):
        self.actualizarSprite()

        # Física de caída
        if self.cayendo:
            self.pos_y += self.speed * 2
            if self.pos_y >= 131:
                self.activo = False
                self.fallado = True
            return

        # Movimiento horizontal en cinta
        cinta_actual = self.cintas[self.indice_cinta]
        self.pos_x += self.speed * cinta_actual.direccion

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, self.u, self.v, 16, 16, 0)

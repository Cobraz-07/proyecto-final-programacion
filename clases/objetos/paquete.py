import pyxel


class Paquete:

    def __init__(self, cintas, velocidad):
        # Recibimos la lista de objetos Cinta desde el Main
        self.cintas = cintas
        self.indice_cinta = 0  # Empezamos en la primera cinta (la de abajo)

        # Obtenemos la cinta actual
        cinta_actual = self.cintas[self.indice_cinta]

        # Posiciones iniciales (abajo a la derecha)
        self.pos_x = 249
        self.pos_y = cinta_actual.y

        self.speed = velocidad  # Velocidad de movimiento
        self.activo = True  # Indica si el paquete está en juego
        self.fallado = False  # Indica si el paquete ha caído
        self.cayendo = False  # Estado cuando cae al vacío

        # Coordenadas del sprite
        self.u = 48
        self.v = 0

    # Método para iniciar la caída del paquete
    def caer(self, x_destino):
        self.pos_x = x_destino
        self.cayendo = True

    def cambiarAltura(self, mario, luigi, camion):
        # Si está cayendo, no puede interactuar
        if self.cayendo:
            return

        # Obtenemos la cinta actual
        cinta_actual = self.cintas[self.indice_cinta]

        # 1. INTERACCIÓN INICIAL (Cinta 0)
        if self.indice_cinta == 0:
            if 180 < self.pos_x <= 197:  # Rango para detectar a velocidad alta
                if mario.posicion == 1:
                    mario.interactuar()
                    self.cambiar_cinta()
                    self.pos_x = 148
                else:
                    self.caer(170)
            return

        # 2. MOVIMIENTO HACIA LA IZQUIERDA
        if cinta_actual.mueve_a_izquierda:
            if self.pos_x <= 72:  # Detectar llegada a la izquierda
                # Calculamos qué posición de Luigi corresponde a esta cinta
                req_pos = (self.indice_cinta // 2) + 1

                if luigi.posicion == req_pos:
                    # Si es la última cinta, entrega al camión
                    if self.indice_cinta == len(self.cintas) - 1:  # Si es la última
                        luigi.interactuar()
                        self.activo = False
                        self.fallado = False  # Entrega exitosa
                    else:
                        # Subir a la siguiente cinta
                        self.cambiar_cinta()
                        self.pos_x = 82
                        camion.sumar_puntos(1)
                else:
                    self.caer(69)
            return

        # 3. MOVIMIENTO HACIA LA DERECHA
        if not cinta_actual.mueve_a_izquierda:  # Dirección 1
            if self.pos_x >= 167:  # Detectar llegada a la derecha
                req_pos = (self.indice_cinta // 2) + 1

                if mario.posicion == req_pos:
                    self.cambiar_cinta()
                    self.pos_x = 154
                    camion.sumar_puntos(1)
                else:
                    self.caer(170)

    def cambiar_cinta(self):
        # Método auxiliar para pasar a la siguiente cinta
        if self.indice_cinta < len(self.cintas) - 1:
            self.indice_cinta += 1
            self.pos_y = self.cintas[self.indice_cinta].y  # Actualizamos la Y al subir de cinta

    def actualizarSprite(self):
        if self.cayendo:
            return

        # Usamos el índice de la cinta para decidir el color (sprite)
        idx = self.indice_cinta

        # Lógica simplificada de sprites basada en índices
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

        # Lógica de caída libre
        if self.cayendo:
            self.pos_y += self.speed * 2
            # Si toca el suelo, se marca como fallado
            if self.pos_y >= 131:
                self.activo = False
                self.fallado = True
            return

        # Movimiento normal en las cintas (zigzag)
        cinta_actual = self.cintas[self.indice_cinta]
        self.pos_x += self.speed * cinta_actual.direccion

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, self.u, self.v, 16, 16, 0)

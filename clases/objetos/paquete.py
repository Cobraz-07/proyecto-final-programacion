import pyxel


class Paquete:
    def __init__(self):
        # Posiciones iniciales (abajo a la derecha)
        self.pos_x = 249
        self.pos_y = 102

        # Alturas de las cintas transportadoras
        self.alturas = [102, 85, 68, 51, 34]

        self.speed = 1  # Velocidad de movimiento
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

        # Interacción inicial con Mario (abajo a la derecha)
        if self.pos_y == self.alturas[0] and self.pos_x == 197:
            if mario.posicion == 1:
                mario.interactuar()
                self.pos_x = 148  # Salto a siguiente cinta
            else:
                self.caer(170)
            return

        # Interacción en la zona izquierda (Luigi)
        if self.pos_x == 72:
            if self.pos_y in self.alturas:
                idx = self.alturas.index(self.pos_y)

                if idx % 2 == 0:
                    req_pos = (idx // 2) + 1  # Calcular posición requerida de Luigi

                    if luigi.posicion == req_pos:
                        # Si es el último nivel, entrega exitosa
                        if req_pos == 3:
                            luigi.interactuar()
                            self.activo = False
                            self.fallado = False
                        else:
                            # Pasar al siguiente nivel
                            self.pos_y = self.alturas[idx + 1]
                            self.pos_x = 82
                            camion.puntos += 1
                    else:
                        self.caer(69)  # Luigi no estaba
            return

        # Interacción en la zona derecha (Mario)
        if self.pos_x == 167:
            if self.pos_y in self.alturas:
                idx = self.alturas.index(self.pos_y)

                if idx % 2 != 0:
                    req_pos = (idx // 2) + 2  # Calcular posición requerida de Mario

                    if mario.posicion == req_pos:
                        # Pasar al siguiente nivel
                        self.pos_y = self.alturas[idx + 1]
                        self.pos_x = 154
                        camion.puntos += 1
                    else:
                        self.caer(170)  # Mario no estaba

    def actualizarSprite(self):
        if self.cayendo:
            return

        # Cambiar sprite según posición en la cinta
        y = self.pos_y
        x = self.pos_x
        h = self.alturas

        # Lógica para seleccionar el sprite correcto del banco de imágenes, dependiendo de la altura y posición
        if y == h[0] and x >= 118:
            self.u, self.v = 48, 0
        elif (y == h[0] or y == h[1]) and x < 118:
            self.u, self.v = 48, 16
        elif (y == h[1] or y == h[2]) and x >= 118:
            self.u, self.v = 48, 32
        elif (y == h[2] or y == h[3]) and x < 118:
            self.u, self.v = 64, 0
        elif (y == h[3] or y == h[4]) and x >= 118:
            self.u, self.v = 64, 16
        else:
            self.u, self.v = 64, 32

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
        if self.pos_y in self.alturas:
            idx = self.alturas.index(self.pos_y)
            # Pares van hacia la derecha, impares a la izquierda
            if idx % 2 == 0:
                self.pos_x -= self.speed
            else:
                self.pos_x += self.speed

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, self.u, self.v, 16, 16, 0)

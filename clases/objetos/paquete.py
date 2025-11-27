import pyxel


class Paquete:
    def __init__(self):
        self.pos_x = 249
        self.pos_y = 102

        self.alturas = [102, 85, 68, 51, 34]

        self.speed = 1

        self.activo = True
        self.fallado = False
        self.cayendo = False

        self.u = 48
        self.v = 0

    def move(self):
        self.actualizarSprite()

        if self.cayendo:
            self.pos_y += self.speed * 2
            if self.pos_y >= 131:
                self.activo = False
                self.fallado = True
            return

        if self.pos_y in self.alturas:
            idx = self.alturas.index(self.pos_y)
            if idx % 2 == 0:
                self.pos_x -= self.speed
            else:
                self.pos_x += self.speed

    def cambiarAltura(self, mario, luigi, camion):
        if self.cayendo:
            return

        def caer(x_destino):
            self.pos_x = x_destino
            self.cayendo = True

        if self.pos_y == self.alturas[0] and self.pos_x == 197:
            if mario.posicion == 1:
                mario.interactuar()
                self.pos_x = 148
            else:
                caer(170)
            return

        if self.pos_x == 72:
            if self.pos_y in self.alturas:
                idx = self.alturas.index(self.pos_y)

                if idx % 2 == 0:
                    req_pos = (idx // 2) + 1

                    if luigi.posicion == req_pos:
                        if req_pos == 3:
                            luigi.interactuar()
                            self.activo = False
                            self.fallado = False
                        else:
                            self.pos_y = self.alturas[idx + 1]
                            self.pos_x = 82
                            camion.puntos += 1
                    else:
                        caer(69)
            return

        if self.pos_x == 167:
            if self.pos_y in self.alturas:
                idx = self.alturas.index(self.pos_y)

                if idx % 2 != 0:
                    req_pos = (idx // 2) + 2

                    if mario.posicion == req_pos:
                        self.pos_y = self.alturas[idx + 1]
                        self.pos_x = 154
                        camion.puntos += 1
                    else:
                        caer(170)

    def actualizarSprite(self):
        if self.cayendo:
            return

        y = self.pos_y
        x = self.pos_x
        h = self.alturas

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

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, self.u, self.v, 16, 16, 0)

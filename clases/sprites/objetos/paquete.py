import pyxel


class Paquete:
    def __init__(self, id):
        self.pos_x = 249
        self.pos_y = 102

        self.altura1 = 102
        self.altura2 = 85
        self.altura3 = 68
        self.altura4 = 51
        self.altura5 = 34

        self.speed = 1
        self.id = id

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

        if self.pos_y == self.altura1:
            self.pos_x -= self.speed
        elif self.pos_y == self.altura2:
            self.pos_x += self.speed
        elif self.pos_y == self.altura3:
            self.pos_x -= self.speed
        elif self.pos_y == self.altura4:
            self.pos_x += self.speed
        elif self.pos_y == self.altura5:
            self.pos_x -= self.speed

    def actualizarSprite(self):
        if self.cayendo:
            return

        if self.pos_y == self.altura1 and self.pos_x >= 118:
            self.u, self.v = 48, 0
        elif (
            self.pos_y == self.altura1 or self.pos_y == self.altura2
        ) and self.pos_x < 118:
            self.u, self.v = 48, 16
        elif (
            self.pos_y == self.altura2 or self.pos_y == self.altura3
        ) and self.pos_x >= 118:
            self.u, self.v = 48, 32
        elif (
            self.pos_y == self.altura3 or self.pos_y == self.altura4
        ) and self.pos_x < 118:
            self.u, self.v = 64, 0
        elif (
            self.pos_y == self.altura4 or self.pos_y == self.altura5
        ) and self.pos_x >= 118:
            self.u, self.v = 64, 16
        else:
            self.u, self.v = 64, 32

    def cambiarAltura(self, mario, luigi, camion):
        if self.cayendo:
            return

        if self.pos_y == self.altura1 and self.pos_x == 205:
            if mario.posicion == 1:
                mario.interactuar()
                self.pos_x = 148
            else:
                self.pos_x = 170
                self.cayendo = True

        elif self.pos_y == self.altura1 and self.pos_x == 82:
            if luigi.posicion == 1:
                self.pos_y = self.altura2
                camion.puntos += 1
            else:
                self.pos_x = 69
                self.cayendo = True

        elif self.pos_y == self.altura2 and self.pos_x == 171:
            if mario.posicion == 2:
                self.pos_y = self.altura3
                camion.puntos += 1
            else:
                self.pos_x = 170
                self.cayendo = True

        elif self.pos_y == self.altura3 and self.pos_x == 82:
            if luigi.posicion == 2:
                self.pos_y = self.altura4
                camion.puntos += 1
            else:
                self.pos_x = 69
                self.cayendo = True

        elif self.pos_y == self.altura4 and self.pos_x == 171:
            if mario.posicion == 3:
                self.pos_y = self.altura5
                camion.puntos += 1
            else:
                self.pos_x = 170
                self.cayendo = True

        elif self.pos_y == self.altura5 and self.pos_x == 82:
            if luigi.posicion == 3:
                luigi.interactuar()
                self.activo = False
                self.fallado = False
            else:
                self.pos_x = 69
                self.cayendo = True

    def draw(self):

        pyxel.blt(self.pos_x, self.pos_y, 0, self.u, self.v, 16, 16, 0)

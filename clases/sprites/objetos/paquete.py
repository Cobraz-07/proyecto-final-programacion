import pyxel
import time


class Paquete:

    def __init__(self):
        self.pos_x = 249
        self.pos_y = 102
        self.altura1 = 102
        self.altura2 = 85
        self.altura3 = 68
        self.altura4 = 51
        self.altura5 = 34
        self.speed = 1

    def move(self):
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

    def cambiarAltura(self, mario, luigi):
        if self.pos_y == self.altura1 and self.pos_x == 205 and mario.posicion == 1:
            mario.interactuar()
            self.pos_x = 148
        elif self.pos_y == self.altura1 and self.pos_x == 205 and mario.posicion != 1:
            self.pos_x = 170
            while self.pos_y < 131:
                self.pos_y += self.speed
        elif self.pos_y == self.altura1 and self.pos_x == 82 and luigi.posicion == 1:
            self.pos_y = self.altura2
        elif self.pos_y == self.altura1 and self.pos_x == 82 and luigi.posicion != 1:
            self.pos_x = 70
            while self.pos_y < 131:
                self.pos_y += self.speed
        elif self.pos_y == self.altura2 and self.pos_x == 171 and mario.posicion == 2:
            self.pos_y = self.altura3
        elif self.pos_y == self.altura2 and self.pos_x == 171 and mario.posicion != 2:
            self.pos_x = 170
            while self.pos_y < 131:
                self.pos_y += self.speed
        elif self.pos_y == self.altura3 and self.pos_x == 82 and luigi.posicion == 2:
            self.pos_y = self.altura4
        elif self.pos_y == self.altura3 and self.pos_x == 82 and luigi.posicion != 2:
            self.pos_x = 70
            while self.pos_y < 131:
                self.pos_y += self.speed
        elif self.pos_y == self.altura4 and self.pos_x == 171 and mario.posicion == 3:
            self.pos_y = self.altura5
        elif self.pos_y == self.altura4 and self.pos_x == 171 and mario.posicion != 3:
            self.pos_x = 170
            while self.pos_y < 131:
                self.pos_y += self.speed

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, 48, 0, 16, 16, 0)

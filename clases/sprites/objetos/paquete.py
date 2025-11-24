import pyxel


class Paquete:

    def __init__(self):
        self.pos_x = 152
        self.pos_y = 35
        self.altura1 = 103
        self.altura2 = 86
        self.altura3 = 69
        self.altura4 = 52
        self.altura5 = 35
        self.speed = 0.5

    def move(self):
        pass

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, 0, 0, 16, 16, 0)

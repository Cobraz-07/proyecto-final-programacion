import pyxel

SCREEN_W = 256
SCREEN_H = 128


class Paquete:

    def __init__(self):
        self.pos_x = (SCREEN_W) // 2
        self.pos_y = (SCREEN_H) // 2
        self.speed = 6

    def move(self):
        self.pos_x -= self.speed

    def draw(self):
        pyxel.blt(self.pos_x, self.pos_y, 0, 0, 0, 16, 16, 0)


paquete = Paquete()

pyxel.init(SCREEN_W, SCREEN_H, title="My Pyxel App")

pyxel.load("./assets/resources.pyxres")
pyxel.images[1].load(0, 0, "./assets/fondo.png")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)

    paquete.draw()


pyxel.run(update, draw)

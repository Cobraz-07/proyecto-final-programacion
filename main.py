import pyxel
from clases.sprites.objetos.paquete import Paquete
from clases.sprites.personajes.mario import Mario

SCREEN_W = 256
SCREEN_H = 144
paquete = Paquete()
mario = Mario()
pyxel.init(SCREEN_W, SCREEN_H)
pyxel.load("./assets/resources.pyxres")
pyxel.images[1].load(0, 0, "./assets/fondo.png")


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)
    paquete.draw()
    mario.draw()


pyxel.run(update, draw)

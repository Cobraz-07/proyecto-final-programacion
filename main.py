import pyxel
from clases.sprites.objetos.paquete import Paquete
from clases.sprites.personajes.mario import Mario
from clases.sprites.personajes.luigi import Luigi

SCREEN_W = 256
SCREEN_H = 144
paquete = Paquete()
mario = Mario()
luigi = Luigi()


class App:
    def __init__(self):
        pyxel.init(SCREEN_W, SCREEN_H)
        pyxel.load("./assets/resources.pyxres")
        pyxel.images[1].load(0, 0, "./assets/fondo.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        mario.move()
        luigi.move()
        paquete.move()
        paquete.cambiarAltura(mario, luigi)

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)
        paquete.draw()
        mario.draw()
        luigi.draw()


App()

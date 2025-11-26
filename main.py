import pyxel
from clases.sprites.objetos.paquete import Paquete
from clases.sprites.personajes.mario import Mario
from clases.sprites.personajes.luigi import Luigi
from clases.sprites.objetos.camion import Camion

SCREEN_W = 256
SCREEN_H = 144

mario = Mario()
luigi = Luigi()
camion = Camion()


class App:
    def __init__(self):
        pyxel.init(SCREEN_W, SCREEN_H)
        pyxel.load("./assets/resources.pyxres")
        pyxel.images[1].load(0, 0, "./assets/fondo.png")
        pyxel.images[2].load(0, 0, "./assets/winscreen.png")

        self.lista_paquetes = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if camion.entregas >= 3:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        if camion.fallos >= 3:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        camion.update()

        if camion.paquetes == 8 and not camion.repartiendo:
            camion.iniciar_reparto()
            self.lista_paquetes.clear()
            return

        if camion.repartiendo:
            return

        mario.move()
        luigi.move()

        if pyxel.frame_count % 210 == 0 and len(self.lista_paquetes) < 3:
            self.lista_paquetes.append(Paquete(len(self.lista_paquetes)))

        for paquete in self.lista_paquetes[:]:
            paquete.move()
            paquete.cambiarAltura(mario, luigi, camion)

            if not paquete.activo:
                if not paquete.fallado:
                    camion.paquetes += 1
                else:
                    camion.fallos += 1

                self.lista_paquetes.remove(paquete)

    def draw(self):
        if camion.entregas >= 3:
            pyxel.cls(0)

            texto1 = "GANASTE!"
            texto2 = "Q para Salir"

            x1 = SCREEN_W // 2 - len(texto1) * 2
            x2 = SCREEN_W // 2 - len(texto2) * 2

            pyxel.text(x1, SCREEN_H // 2 - 10, texto1, 3)
            pyxel.text(x1, SCREEN_H // 2 - 50, "Puntos: " + str(camion.puntos), 3)
            pyxel.text(x2, SCREEN_H // 2 + 10, texto2, 7)
            return

        if camion.fallos >= 3:
            pyxel.cls(0)

            texto1 = "GAME OVER"
            texto2 = "Q para Salir"

            x1 = SCREEN_W // 2 - len(texto1) * 2
            x2 = SCREEN_W // 2 - len(texto2) * 2

            pyxel.text(x1, SCREEN_H // 2 - 10, texto1, 8)
            pyxel.text(x2, SCREEN_H // 2 + 10, texto2, 7)
            return

        pyxel.cls(0)
        pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)

        pyxel.text(2, 2, f"Puntos: {camion.puntos}", 3)
        pyxel.text(45, 2, f"Fallos: {camion.fallos}/3", 8)

        for paquete in self.lista_paquetes:
            paquete.draw()

        mario.draw()
        luigi.draw()
        camion.draw()


App()

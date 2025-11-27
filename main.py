import pyxel
from clases.objetos.paquete import Paquete
from clases.personajes.mario import Mario
from clases.personajes.luigi import Luigi
from clases.objetos.camion import Camion
from clases.personajes.jefe import Jefe

SCREEN_W = 256
SCREEN_H = 144

mario = Mario()
luigi = Luigi()
camion = Camion()
jefe = Jefe()


class App:
    def __init__(self):
        pyxel.init(SCREEN_W, SCREEN_H)
        pyxel.load("./assets/resources.pyxres")
        pyxel.images[1].load(0, 0, "./assets/fondo.png")

        self.lista_paquetes = []
        pyxel.run(self.update, self.draw)

    def dibujar_texto_centrado(self, texto, y, color):
        x = SCREEN_W // 2 - len(texto) * 2
        pyxel.text(x, y, texto, color)

    def mostrar_pantalla_final(self, titulo, color_titulo, es_victoria):
        pyxel.cls(0)

        self.dibujar_texto_centrado(titulo, SCREEN_H // 2 - 10, color_titulo)
        self.dibujar_texto_centrado("Q para Salir", SCREEN_H // 2 + 10, 7)

        if es_victoria:
            self.dibujar_texto_centrado(
                f"Puntos: {camion.puntos}", SCREEN_H // 2 - 50, 3
            )
            mario.drawVictoria(SCREEN_W // 2 - 66, SCREEN_H // 2 + 10)
            luigi.drawVictoria(SCREEN_W // 2 + 50, SCREEN_H // 2 + 10)

    def update(self):
        if camion.entregas == 3 or camion.fallos == 3:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        jefe.update()
        if jefe.regañando:
            return

        entregas_antes = camion.entregas
        camion.update()

        if camion.entregas > entregas_antes:
            jefe.aparecerDoble()

        if camion.repartiendo:
            if camion.paquetes == 8:
                self.lista_paquetes.clear()
            return

        if camion.paquetes == 8 and not camion.repartiendo:
            camion.iniciar_reparto()
            self.lista_paquetes.clear()
            return

        mario.move()
        luigi.move()

        if pyxel.frame_count % 210 == 0 and len(self.lista_paquetes) < 3:
            self.lista_paquetes.append(Paquete())

        for paquete in self.lista_paquetes[:]:
            paquete.move()
            paquete.cambiarAltura(mario, luigi, camion)

            if not paquete.activo:
                if not paquete.fallado:
                    camion.paquetes += 1
                else:
                    camion.fallos += 1
                    jefe.aparecer(paquete.pos_x)

                self.lista_paquetes.remove(paquete)

    def draw(self):
        if camion.entregas == 3:
            self.mostrar_pantalla_final("GANASTE!", 3, es_victoria=True)
            return

        if camion.fallos == 3:
            self.mostrar_pantalla_final("GAME OVER", 8, es_victoria=False)
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
        jefe.draw()


App()

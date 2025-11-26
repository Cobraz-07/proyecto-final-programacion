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

        # Carga segura de imágenes (asegúrate que existen estos archivos)
        try:
            pyxel.images[1].load(0, 0, "./assets/fondo.png")
            pyxel.images[2].load(0, 0, "./assets/winscreen.png")
        except:
            pass  # Si no existen, usará lo que haya en resources

        self.lista_paquetes = []
        pyxel.run(self.update, self.draw)

    def update(self):
        # Condición de victoria
        if camion.entregas >= 3:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        camion.update()

        # Si el camión está lleno y no ha empezado a irse
        if camion.paquetes == 8 and not camion.repartiendo:
            camion.iniciar_reparto()
            self.lista_paquetes.clear()  # Limpia paquetes al salir
            return

        # Si el camión está repartiendo, pausa el juego
        if camion.repartiendo:
            return

        # --- JUEGO ACTIVO ---

        mario.move()
        luigi.move()

        # Generación de paquetes:
        if pyxel.frame_count % 120 == 0 and len(self.lista_paquetes) < 3:
            self.lista_paquetes.append(Paquete(len(self.lista_paquetes)))

        for paquete in self.lista_paquetes[:]:
            paquete.move()
            paquete.cambiarAltura(mario, luigi)

            if not paquete.activo:
                if not paquete.fallado:
                    camion.paquetes += 1
                self.lista_paquetes.remove(paquete)

    def draw(self):
        # Pantalla de victoria
        if camion.entregas >= 3:
            pyxel.cls(0)
            pyxel.blt(0, 0, 2, 0, 0, SCREEN_W, SCREEN_H)
            return

        pyxel.cls(0)
        pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)

        # Dibujamos paquetes (la lista estará vacía durante la pausa)
        for paquete in self.lista_paquetes:
            paquete.draw()

        mario.draw()
        luigi.draw()
        camion.draw()


App()

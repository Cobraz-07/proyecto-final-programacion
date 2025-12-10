import pyxel
from clases.objetos.paquete import Paquete
from clases.personajes.mario import Mario
from clases.personajes.luigi import Luigi
from clases.objetos.camion import Camion
from clases.personajes.jefe import Jefe
from clases.objetos.cinta import Cinta

# Configuración global
SCREEN_W = 256
SCREEN_H = 144
VELOCIDAD_PAQUETES = 1
FRAMES_POR_PAQUETE = 210

# Instancias globales
mario = Mario()
luigi = Luigi()
camion = Camion()
jefe = Jefe()


class App:
    def __init__(self):
        # Inicio Pyxel y carga de recursos
        pyxel.init(SCREEN_W, SCREEN_H)
        pyxel.load("./assets/resources.pyxres")
        pyxel.images[1].load(0, 0, "./assets/fondo.png")

        # Define sonido de arranque del camión
        pyxel.sounds[2].set("c0e0g0c1", "p", "3567", "s", 50)

        # Inicializa cintas y lista de paquetes
        self.cintas_juego = [Cinta(102, -1), Cinta(102, -1), Cinta(85, 1), Cinta(68, -1), Cinta(51, 1), Cinta(34, -1)]
        self.lista_paquetes = []

        pyxel.run(self.update, self.draw)

    def play_regaño(self):
        # Reproduce sonido en canal 0
        pyxel.playm(0, loop=False)

    def play_cambio_de_altura(self):
        # Reproduce sonido corto en canal 1
        pyxel.play(1, 1)

    def dibujar_texto_centrado(self, texto, y, color):
        # Centra texto horizontalmente en pantalla
        x = SCREEN_W // 2 - len(texto) * 2
        pyxel.text(x, y, texto, color)

    def mostrar_pantalla_final(self, titulo, color_titulo):
        pyxel.cls(0)
        self.dibujar_texto_centrado(titulo, SCREEN_H // 2 - 10, color_titulo)
        self.dibujar_texto_centrado("Q para Salir", SCREEN_H // 2 + 10, 7)

    def update(self):
        # Verifica condición de Game Over
        if camion.fallos == 3:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        # Gestiona estado del jefe
        jefe.update()
        if jefe.regañando:
            return

        # Gestiona camión y bonificaciones
        entregas_antes = camion.entregas
        camion.update()
        if camion.entregas > entregas_antes:
            jefe.aparecerDoble()

        # Pausa generación si el camión se va
        if camion.repartiendo:
            return

        # Inicia reparto si está lleno
        if camion.paquetes == 8 and not camion.repartiendo:
            camion.iniciar_reparto()
            self.lista_paquetes.clear()
            return

        # Actualiza personajes
        mario.move()
        luigi.move()

        # Genera nuevos paquetes periódicamente
        if pyxel.frame_count % FRAMES_POR_PAQUETE == 0 and len(self.lista_paquetes) < 3:
            self.lista_paquetes.append(Paquete(self.cintas_juego, VELOCIDAD_PAQUETES, self.play_cambio_de_altura))

        # Gestiona física y lógica de paquetes
        for paquete in self.lista_paquetes[:]:
            paquete.move()
            paquete.cambiar_altura(mario, luigi, camion)

            # Procesa paquetes finalizados
            if not paquete.activo:
                if not paquete.fallado:
                    camion.cargar_paquete()
                else:
                    camion.registrar_fallo()
                    jefe.aparecer(paquete.pos_x)
                    self.play_regaño()
                self.lista_paquetes.remove(paquete)

    def draw(self):
        # Dibuja pantalla de fin si corresponde
        if camion.fallos == 3:
            self.mostrar_pantalla_final("GAME OVER", 8)
            return

        # Renderizado general del juego
        pyxel.cls(0)
        pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)
        pyxel.text(2, 2, f"Puntos: {camion.puntos}", 3)
        pyxel.text(50, 2, f"Fallos: {camion.fallos}/3", 8)

        for paquete in self.lista_paquetes:
            paquete.draw()
        mario.draw()
        luigi.draw()
        camion.draw()
        jefe.draw()


App()

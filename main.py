import pyxel
from clases.objetos.paquete import Paquete
from clases.personajes.mario import Mario
from clases.personajes.luigi import Luigi
from clases.objetos.camion import Camion
from clases.personajes.jefe import Jefe
from clases.objetos.cinta import Cinta

# Configuración de tamaño pantalla
SCREEN_W = 256
SCREEN_H = 144

# Dificultad
VELOCIDAD_PAQUETES = 1
FRAMES_POR_PAQUETE = 210

# Instancia global de objetos
mario = Mario()
luigi = Luigi()
camion = Camion()
jefe = Jefe()


class App:
    def __init__(self):
        # Inicialización de Pyxel y carga de recursos
        pyxel.init(SCREEN_W, SCREEN_H)
        pyxel.load("./assets/resources.pyxres")
        # Cargar imagen de fondo en el banco de imágenes 1
        pyxel.images[1].load(0, 0, "./assets/fondo.png")

        pyxel.sounds[2].set("c0e0g0c1", "p", "3567", "s", 50)

        self.cintas_juego = [Cinta(102, -1), Cinta(102, -1), Cinta(85, 1), Cinta(68, -1), Cinta(51, 1), Cinta(34, -1)]
        self.lista_paquetes = []

        pyxel.run(self.update, self.draw)

    def play_regaño(self):
        pyxel.playm(0, loop=False)

    def play_cambio_de_altura(self):
        pyxel.play(1, 1)

    def dibujar_texto_centrado(self, texto, y, color):
        # Calcula la posición X para centrar el texto
        x = SCREEN_W // 2 - len(texto) * 2
        pyxel.text(x, y, texto, color)

    def mostrar_pantalla_final(self, titulo, color_titulo, es_victoria):
        pyxel.cls(0)

        # Mostrar títulos
        self.dibujar_texto_centrado(titulo, SCREEN_H // 2 - 10, color_titulo)
        self.dibujar_texto_centrado("Q para Salir", SCREEN_H // 2 + 10, 7)

        # Si gana, mostrar puntuación y animación de victoria
        if es_victoria:
            self.dibujar_texto_centrado(f"Puntos: {camion.puntos}", SCREEN_H // 2 - 50, 3)
            mario.drawVictoria(SCREEN_W // 2 - 66, SCREEN_H // 2 + 10)
            luigi.drawVictoria(SCREEN_W // 2 + 50, SCREEN_H // 2 + 10)

    def update(self):
        # Verificar fin del juego (3 entregas o 3 fallos)
        if camion.entregas == 3 or camion.fallos == 3:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return

        # Actualizar al Jefe (animación de regaño)
        jefe.update()
        if jefe.regañando:
            return  # Pausar el juego si el jefe está regañando

        # Lógica del camión y entregas
        entregas_antes = camion.entregas
        camion.update()

        # Si se completa una entrega, el jefe aparece doble para avisar de que dejen de descansar
        if camion.entregas > entregas_antes:
            jefe.aparecerDoble()

        # Si el camión se está yendo, pausar generación de paquetes
        if camion.repartiendo:
            return

        # Si el camión está lleno (8 paquetes), iniciar reparto
        if camion.paquetes == 8 and not camion.repartiendo:
            camion.iniciar_reparto()
            self.lista_paquetes.clear()
            return

        # Movimiento de personajes
        mario.move()
        luigi.move()

        # Generar paquetes nuevos periódicamente (máximo 3 en pantalla)
        if pyxel.frame_count % FRAMES_POR_PAQUETE == 0 and len(self.lista_paquetes) < 3:
            self.lista_paquetes.append(Paquete(self.cintas_juego, VELOCIDAD_PAQUETES, self.play_cambio_de_altura))

        # Actualizar paquetes existentes
        for paquete in self.lista_paquetes[:]:
            paquete.move()
            paquete.cambiar_altura(mario, luigi, camion)

            # Gestión de paquetes inactivos (entregados o caídos)
            if not paquete.activo:
                if not paquete.fallado:
                    camion.cargar_paquete()  # Paquete exitoso
                else:
                    camion.registrar_fallo()  # Paquete fallido
                    jefe.aparecer(paquete.pos_x)  # Jefe regaña en la posición del fallo
                    self.play_regaño()

                self.lista_paquetes.remove(paquete)

    def draw(self):
        # Pantallas de fin de juego
        if camion.entregas == 3:
            self.mostrar_pantalla_final("GANASTE!", 3, es_victoria=True)
            return

        if camion.fallos == 3:
            self.mostrar_pantalla_final("GAME OVER", 8, es_victoria=False)
            return

        # Borrar la pantalla
        pyxel.cls(0)
        # Dibujar el fondo
        pyxel.blt(0, 0, 1, 0, 0, SCREEN_W, SCREEN_H)

        # Interfaz de puntos y fallos
        pyxel.text(2, 2, f"Puntos: {camion.puntos}", 3)
        pyxel.text(50, 2, f"Fallos: {camion.fallos}/3", 8)

        # Dibujar paquetes
        for paquete in self.lista_paquetes:
            paquete.draw()

        mario.draw()
        luigi.draw()
        camion.draw()
        jefe.draw()


App()

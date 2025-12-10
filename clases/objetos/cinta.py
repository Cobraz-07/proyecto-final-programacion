class Cinta:
    def __init__(self, y, direccion):
        self.y = y
        # Dirección: -1 (Izquierda), 1 (Derecha)
        self.direccion = direccion

    @property
    def mueve_a_izquierda(self):
        # Ayuda visual para saber la dirección del flujo
        return self.direccion == -1

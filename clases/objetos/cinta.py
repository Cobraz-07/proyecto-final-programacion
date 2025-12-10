class Cinta:
    def __init__(self, y, direccion):
        self.y = y
        self.direccion = direccion  # -1 para izquierda, 1 para derecha

    @property
    def mueve_a_izquierda(self):
        return self.direccion == -1

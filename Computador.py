class Computador:
    contador_computadoras = 0
    id_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
class Computador:
    contador_computadoras = 0
    id_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computador.id_computadora += 1
        Computador.contador_computadoras += 1
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @monitor.setter
    def nombre(self, monitor):
        self._monitor = monitor

    @teclado.setter
    def nombre(self, teclado):
        self._teclado = teclado

    @nombre.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'Id : {Computador.id_computadora}, \n Nombre : {self._nombre}'


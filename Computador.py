
class Computador:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador_computadoras += 1
        self._id_computador = Computador.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
         {self._nombre} : {self._id_computador}
         Monitor : {self._teclado}
         Teclado : {self._teclado}
         Raton : {self._raton}
         '''





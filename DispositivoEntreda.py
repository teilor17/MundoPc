class DispoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @property
    def marca(self):
        return self._marca

    @tipoEntrada.setter
    def tipoEntreda(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Tipo de Entrada : {self._tipoEntrada}, Marca : {self._marca}'
    
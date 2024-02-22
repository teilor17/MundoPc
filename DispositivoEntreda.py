class DispoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def __str__(self):
        return f'Tipo de Entrada : {self._tipoEntrada}, Marca : {self._marca}'

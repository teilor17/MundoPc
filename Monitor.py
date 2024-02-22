class Monitor:
    contador_monitor = 0
    id_monitor = 0
    def __init__(self, marca, tamaño):
        self._marca = marca
        self._tamaño = tamaño

    @property
    def marca(self):
        return self._mara

    @property
    def tamaño(self):
        return self._tamaño

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @tamaño.setter
    def tamaño(self,tamaño):
        self._tamaño = tamaño

    def __str__(self):
        return f'Marca : {self._marca}, Tamaño : {self._tamaño}'

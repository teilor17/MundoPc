from DispositivoEntreda import DispoEntrada
class Raton(DispoEntrada):
    contador_ratones = 0
    def __init__(self,tipoEntrada, marca):
        Raton.contador_ratones +=1
        super().__init__(tipoEntrada, marca)
        self._id_raton = Raton.contador_ratones
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Id : {self._id_raton}, Marca : {self._marca}, Tipo entrada : {self._tipoEntrada}'


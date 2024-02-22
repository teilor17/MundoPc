from DispositivoEntreda import DispoEntrada
class Teclado(DispoEntrada):
    contador_teclado = 0
    def __init__(self,tipoEntrada, marca):
        Teclado.contador_teclado +=1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(tipoEntrada, marca)


    def __str__(self):
        return f'Id : {self._id_teclado}, Marca : {self._marca}, Tipo entrada : {self._tipoEntrada}'


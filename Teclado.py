from DispositivoEntreda import DispoEntrada
class Teclado(DispoEntrada):
    contador_teclado = 0
    id_teclado = 0
    def __init__(self,tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return

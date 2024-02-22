from DispositivoEntreda import DispoEntrada
class Raton(DispoEntrada):
    contador_ratones = 0
    id_raton = 0
    def __init__(self,tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return


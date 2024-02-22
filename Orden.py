class Orden:
    contador_orden = 0
    def __init__(self,computadores):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._computadoras = list(computadores)

    def agregar_computadores(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
                Orden : {self._id_orden}
                Computadoras : {computadoras_str}
                '''


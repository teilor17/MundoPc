from Computador import Computador
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

teclado1 = Teclado('USB', 'HP')
raton1 = Raton('BLTH', 'DELL')
monitor1 = Monitor('DELL', '1080')

teclado2 = Teclado('BLTH', 'HP')
raton2 = Raton('USB', 'DELL')
monitor2 = Monitor('TOSHIA', '2040')

teclado3 = Teclado('USB', 'QBEX')
raton3 = Raton('USB', 'QBEX')
monitor3 = Monitor('QBEX', '2040')

computador1 = Computador('Asus', monitor2, teclado1, raton3)
computador2 = Computador('Gamer', monitor1, teclado1, raton3)
computador3 = Computador('hp', monitor3, teclado3, raton2)

computadores1 = [computador3, computador2]
computadores2 = [computador3, computador2, computador1]
computadores3 = [computador1, computador2]

ordenA = Orden(computadores1)
ordenA.agregar_computadores(computador1)
print(ordenA)

ordenB = Orden(computadores2)
print(ordenB)

ordenC = Orden(computadores3)
ordenC.agregar_computadores(computador2)
print(ordenC)
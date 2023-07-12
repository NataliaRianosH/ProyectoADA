import main 
import solucionOptimizada
import time

inicio = time.time()

n = 100
m = 6
k = 3

animales = [
    ("caballo", 9),
    ("serpiente", 3),
    ("mula", 7),
    ("conejo", 1),
    ("cabra", 4),
    ("gato", 2),
    ("salamandra", 6),
    ("perro", 5),
    ("tortuga", 8)
]

apertura = [["tortuga", "caballo", "cabra"], ["tortuga", "perro", "serpiente"], ["serpiente", "mula", "conejo"], ["gato", "caballo", "conejo"], ["serpiente", "mula", "cabra"],
            ["perro", "serpiente", "mula"], ["salamandra", "caballo", "serpiente"], ["salamandra", "caballo", "conejo"], ["salamandra", "mula", "gato"], ["salamandra", "tortuga", "perro"],
            ["mula", "conejo", "gato"],  ["salamandra", "perro", "cabra"], ["serpiente","salamandra", "gato"], ["mula", "cabra", "perro"], ["tortuga", "salamandra", "gato"]]

parte1=[["tortuga", "caballo", "cabra"],["perro", "serpiente","gato"], ["mula","conejo","salamandra"]]
parte2=[["tortuga", "perro","mula"], ["perro","salamandra","gato"], ["conejo", "tortuga", "cabra"]]
parte3=[["tortuga", "conejo", "cabra"], ["tortuga", "gato","caballo"], ["salamandra","mula","serpiente"]]
parte4=[["tortuga", "caballo", "serpiente"], ["perro", "serpiente", "mula"], ["tortuga", "mula","serpiente"]]
parte5=[["mula", "salamandra", "perro"], ["salamandra", "gato", "caballo"], ["salamandra", "conejo", "perro"]]
partes = [parte5, parte4, parte3, parte2, parte1]

solucionOptimizada.espectaculo(n,m,k,animales,apertura,partes)

final = time.time()
print (final-inicio)
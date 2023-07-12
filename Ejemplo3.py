import main
import time

inicio = time.time()

n = 9
m = 4
k = 3

animales = [
    ("leon", 9),
    ("panteranegra", 7),
    ("cebra", 6),
    ("cocodrilo", 5),
    ("boa", 4),
    ("loro", 2),
    ("caiman", 3),
    ("tigre", 8),
    ("capibara", 1)
]

apertura = [["caiman", "capibara", "loro"], ["boa", "caiman", "capibara"], ["cocodrilo", "capibara", "loro"], ["panteranegra", "cocodrilo", "loro"], ["tigre", "loro", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"], ["leon", "panteranegra", "cebra"], ["tigre", "cebra", "panteranegra"]]

parte1 = [["caiman", "capibara", "loro"], ["tigre", "loro", "capibara"], ["tigre", "cebra", "panteranegra"]]

parte2 = [["panteranegra", "cocodrilo", "loro"], ["leon", "panteranegra", "cebra"], ["cocodrilo", "capibara", "loro"]]

parte3 = [["boa", "caiman", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"]]

partes=[parte3, parte2,parte1]

main.espectaculo(n,m,k,animales,apertura,partes)

final = time.time()
print (final-inicio)

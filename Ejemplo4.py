import main 
import time

inicio = time.time()

n = 9
m = 4
k = 3

animales = [
    ("capibara", 1),
    ("loro", 2),
    ("caiman", 3),
    ("boa", 4),
    ("cocodrilo", 5),
    ("cebra", 6),
    ("pantera negra", 7),
    ("tigre", 8),
    ("leon", 9)
]

apertura = [["caiman","capibara","loro"], ["boa","caiman","capibara"], ["cocodrilo","capibara","loro"], 
           ["pantera negra","cocodrilo","loro"], ["tigre","loro","capibara"], ["leon","caiman","loro"], 
           ["leon","cocodrilo","boa"], ["leon","pantera negra","cebra"], ["tigre","cebra","pantera negra"]]

parte1=[["caiman","capibara","loro"],["tigre","loro","capibara"], ["tigre","cebra","pantera negra"]]
parte2=[["pantera negra","cocodrilo","loro"], ["leon","pantera negra","cebra"], ["cocodrilo","capibara","loro"]]
parte3=[["boa","caiman","capibara"], ["leon","caiman","loro"], ["leon","cocodrilo","boa"]]
partes = [parte1, parte2, parte3]

main.espectaculo(n,m,k,animales,apertura,partes)

final = time.time()
print (final-inicio)
import solucion
n = 9
m = 4
k = 3

animales = ["capibara", "loro", "caiman", "boa", "cocodrilo", "cebra", "pantera negra", "tigre", "leon"]
grandezas = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

apertura = [["caiman", "capibara", "loro"], ["boa", "caiman", "capibara"], ["cocodrilo", "capibara", "loro"], 
            ["pantera negra", "cocodrilo", "loro"], ["tigre", "loro", "capibara"], ["leon", "caiman", "loro"], 
            ["leon", "cocodrilo", "boa"], ["leon", "pantera negra", "cebra"], ["tigre", "cebra", "pantera negra"]]

parte1 = [["caiman", "capibara", "loro"], ["tigre", "loro", "capibara"], ["tigre", "cebra", "pantera negra"]]
parte2 = [["pantera negra", "cocodrilo", "loro"], ["leon", "pantera negra", "cebra"], ["cocodrilo", "capibara", "loro"]]
parte3 = [["boa", "caiman", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"]]

partes = [parte1, parte2, parte3]

solucion.espectaculo(n, m, k, animales, grandezas, apertura, partes)

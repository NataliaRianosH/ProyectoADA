import Algoritmos.solucion as solucion
n = 9
m = 4
k = 3

n = 9
m = 4
k = 3

animales = ['leon', 'panteranegra', 'cebra', 'cocodrilo', 'boa', 'loro', 'caiman', 'tigre', 'capibara']

grandezas = [9, 7, 6, 5, 4, 2, 3, 8, 1]

apertura = [['caiman', 'capibara', 'loro'], ['boa', 'caiman', 'capibara'], ['cocodrilo', 'capibara', 'loro'], ['panteranegra', 'cocodrilo', 'loro'], ['tigre', 'loro', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa'], ['leon', 'panteranegra', 'cebra'], ['tigre', 'cebra', 'panteranegra']]

parte1 = [['caiman', 'capibara', 'loro'], ['tigre', 'loro', 'capibara'], ['tigre', 'cebra', 'panteranegra']]

parte2 = [['panteranegra', 'cocodrilo', 'loro'], ['leon', 'panteranegra', 'cebra'], ['cocodrilo', 'capibara', 'loro']]

parte3 = [['boa', 'caiman', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa']]

partes=[parte2,parte3,parte1]
r = solucion.espectaculo(n,m,k,animales,grandezas, apertura, partes)
solucion.visualizarResultado(r)
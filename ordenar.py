
import grandeza
#Para hacer pruebas:
n = 9
m = 4
k = 3

animales = ["capibara", "loro", "caiman", "boa", "cocodrilo", "cebra", "pantera negra", "tigre", "leon"]
grandezas = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
apertura=[[3, 1, 2], [4, 3, 1], [5, 1, 2], [7, 5, 2], [8, 2, 1], [9, 3, 2], [9, 5, 4], [9, 7, 6], [8, 6, 7]]
parte1= [[3, 1, 2], [8, 2, 1], [8, 6, 7]]
parte2= [[7, 5, 2], [9, 7, 6], [5, 1, 2]]
parte3= [[4, 3, 1], [9, 3, 2], [9, 5, 4]]

partes=[parte1,parte2,parte3]

"""
  m= cant de partes
  m-1=partes sin apertura
  k=cant de escenas en cada parte 
  (m-1)*k 
  cada escena siempre tiene 3 animes

Traducir apertura así:
print(apertura)
traducir.parteToAnimal(animales, grandezas, apertura, (m-1)*k)
print(apertura) 

"""
#O(1) las escenas siempre van a tener 3 animales
def escena(numeros):
    nums=numeros[:]
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2], nums[1]
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
    return nums

# O(k^2), cuadratica con respecto a K
def parte(parte, k):
    for i in range(k):
        parte[i] = escena(parte[i])

    for i in range(k-1):
        for j in range(i+1, k):
            if grandeza.escena(parte[j]) < grandeza.escena(parte[i]):
                parte[i], parte[j] = parte[j], parte[i]
            elif grandeza.escena(parte[j]) == grandeza.escena(parte[i]):
                max_i = max(parte[i])
                max_j = max(parte[j])
                if max_j < max_i:
                    parte[i], parte[j] = parte[j], parte[i]
    return parte

#O(m^2 * k), cuadratica con respecto a m y lineal con respecto a k
def listaDePartes(partes, m, k):
    m=m-1
    for i in range(m):
        partes[i] = parte(partes[i], k)  

    for i in range(m-1):
        max_index = i
        for j in range(i+1, m):
            if grandeza.parte(partes[j], k) < grandeza.parte(partes[max_index], k):
                max_index = j
            elif grandeza.parte(partes[j], k) == grandeza.parte(partes[max_index], k):
                max_j = max(max(parte) for parte in partes[j])
                max_max_index = max(max(parte) for parte in partes[max_index])
                if max_j < max_max_index:
                    max_index = j
        partes[i], partes[max_index] = partes[max_index], partes[i]
    return partes

#O((m-1)*k), lineal con respecto a k
def apertura(apertura, m, k):
    #como la apertura es una parte podemos usar ordenar parte
    parte(apertura, (m-1)*k)
    return apertura

#PRUEBAS:
#print("partes:" , ordenarListaDePartes(partes, 4, 3))
#print(ordenarListaDePartes([ [[2,3,2], [1,3,1]] , [[5,3,5], [3,3,3]]], 2, 2 ))
#print(ordenarListaDePartes([ [[4, 8, 8], [3, 7,10]], [[7,7,6], [5,6,9]]], 2, 2 ))

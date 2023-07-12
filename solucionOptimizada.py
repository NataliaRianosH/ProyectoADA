#la escena siempre tendrá 3 elementos, tonces:
apertura=[[3, 1, 2], [4, 3, 1], [5, 1, 2], [7, 5, 2], [8, 2, 1], [9, 3, 2], [9, 5, 4], [9, 7, 6], [8, 6, 7]]
partes=[ [[3, 1, 2], [4, 3, 1], [5, 1, 2]],
         [[7, 5, 2], [9, 7, 6], [5, 1, 2]],
         [[4, 3, 1], [9, 3, 2], [9, 5, 4]]
         ]
#O(1)
def ordenarEscena(nums):
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2], nums[1]
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
    return nums

#print(ordenarEscena([3,2,1]))
#O(1)
def grandezaEscena(escena):
   return escena[0]+ escena[1]+ escena[2]

#parte esta compuesra de escenas [[7,8,9],[1,2,3], [4,5,6]]
#k escenas de cada parte-> tamaño de parte
# odenar teniendo en cuenra la grandeza de cada escena
#complejidad O(k^2)=O(k) lineal
def ordenarParte(parte, k):
    for i in range(k):
        parte[i] = ordenarEscena(parte[i])

    for i in range(k-1):
        for j in range(i+1, k):
            if grandezaEscena(parte[j]) < grandezaEscena(parte[i]):
                parte[i], parte[j] = parte[j], parte[i]
            elif grandezaEscena(parte[j]) == grandezaEscena(parte[i]):
                max_i = max(parte[i])
                max_j = max(parte[j])
                if max_j < max_i:
                    parte[i], parte[j] = parte[j], parte[i]
    return parte

#print(ordenarParte([[7,1,4],[5,3,4],[2,3,2],[4,3,4]], 4))
#print(ordenarParte([[3,3,3],[1,3,1],[2,3,2],[4,3,4]], 4))
#print(ordenarParte([[3, 1, 2], [4, 3, 1], [5, 1, 2], [7, 5, 2], [8, 2, 1], [9, 3, 2], [9, 5, 4], [9, 7, 6], [8, 6, 7]], 9))



#Retornar la grandeza de una parte
#k=cant de escenas en cada parte 
#parte es [[7,8,9],[1,2,3], [4,5,6]]
#calcula la suma de las grandezas las k escenas
# tambien se hace k veces tonces O(k)=O(1)
def grandezaParte(parte, k):
   suma_grandezas = 0
   for i in range(k):
       suma_grandezas += grandezaEscena(parte[i])
   return suma_grandezas

#print(grandezaParte([[1,2,3], [1,1,1], [1,1,1]], 3))


#partes es una lista que contiene partes, ejemplo ()
#m es la cantidad de partes que hay
#siguiendo la logica anterior, se ordenan las m partes dependiendo de la grandeza de las k escenas que componen las partes 
#complejidad O(m*k) lineal con respecto al numero de escenas
# hacer que en caso de q ambas grandezas sean iguales hacer esto:
# por ejemplo si partes= [[4, 8, 8], [3, 7,10]], [[7,7,6], [5,6,9]] 
# retona [[[6, 7, 7], [5, 6, 9]] , [[4, 8, 8, [3, 7,10]]]
# porque el mayor de [[7,7,6], [5,6,9]] es 9 y el mayor de [[4, 8, 8], [3, 7,10]] es 10 y 9<10

def ordenarListaDePartes(partes, m, k):
    m=m-1
    for i in range(m):
        partes[i] = ordenarParte(partes[i], k)  

    for i in range(m-1):
        max_index = i
        for j in range(i+1, m):
            if grandezaParte(partes[j], k) < grandezaParte(partes[max_index], k):
                max_index = j
            elif grandezaParte(partes[j], k) == grandezaParte(partes[max_index], k):
                max_j = max(max(parte) for parte in partes[j])
                max_max_index = max(max(parte) for parte in partes[max_index])
                if max_j < max_max_index:
                    max_index = j
        partes[i], partes[max_index] = partes[max_index], partes[i]
    return partes
#print("partes:" , ordenarListaDePartes(partes, 4, 3))
#print(ordenarListaDePartes([ [[2,3,2], [1,3,1]] , [[5,3,5], [3,3,3]]], 2, 2 ))
#print(ordenarListaDePartes([ [[4, 8, 8], [3, 7,10]], [[7,7,6], [5,6,9]]], 2, 2 ))
"""
             m= cant de partes, sin la apertira
             k=cant de escenas en cada parte 
             cada escena siempre tiene 3 animes
"""
def ordenarApertura(apertura, m, k):
    return ordenarParte(apertura, (m-1)*k)

#print(ordenarApertura(apertura, 4, 3))


def espectaculo(n, m, k, animales, apertura, partes):
    return ordenarApertura(apertura, m, k) , ordenarListaDePartes(partes, m ,k)

print(espectaculo(4, 3, apertura, partes)[0])
print(espectaculo(4, 3, apertura, partes)[1])


"""
lista-> lista conformada por varias listas
def comprimir(lista):
    #retorna solo los elementos internos de la lista
    return
ejemplo comprimir([[1],[1,3,5],[[5]]]) retorne [1,1,3,5,5]
    """

def comprimir(lista):
    resultado = []
    for sublist in lista:
        if isinstance(sublist, list):  # si el elemento de la lista es otra lista
            resultado.extend(comprimir(sublist))  # llamamos recursivamente a la función para esa lista interna
        else:
            resultado.append(sublist)  # si no es una lista simplemente lo agregamos a la lista de resultados
    return resultado
print(comprimir(partes))

def moda(apertura, partes):
    completo=comprimir(apertura)+ comprimir(partes)
    return 

print(moda(apertura, partes))
"""
def comprimir(apertura, partes):
    #retorna una lista con todos los elementos de apertura y partes
    return 
apertura son listas de este estilo [[1, 2, 3], [1, 3, 4], [1, 2, 5], [1, 2, 8], [2, 5, 7], [2, 3, 9], [4, 5, 9], [6, 7, 8], [6, 7, 9]]
partes son listas de este estilo [[[1, 2, 3], [1, 3, 4], [1, 2, 5]], [[1, 3, 4], [2, 3, 9], [4, 5, 9]], [[1, 2, 5], [2, 5, 7], [6, 7, 9]]]
"""
#la escena siempre tendrá 3 elementos, tonces:
apertura=[[3, 1, 2], [4, 3, 1], [5, 1, 2], [7, 5, 2], [8, 2, 1], [9, 3, 2], [9, 5, 4], [9, 7, 6], [8, 6, 7]]
partes=[ 
         [[3, 1, 2], [8, 2, 1], [8, 6, 7]],
         [[7, 5, 2], [9, 7, 6], [5, 1, 2]],
         [[4, 3, 1], [9, 3, 2], [9, 5, 4]]
         ]

#O(1) las escenas siempre van a tener 3 animales
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

def ordenarApertura(apertura, m, k):
    #como la apertura es una parte podemos usar ordenar parte
    return ordenarParte(apertura, (m-1)*k)
#print(ordenarApertura(apertura, 4, 3))
#print(espectaculo(4, 3, apertura, partes)[0])
#print(espectaculo(4, 3, apertura, partes)[1])

###ANALISIS HASTA AQUÍ

#Las primeras m-1 listas tienen k escenas (osea q son de tamaño k)
#cada escena tiene siempre 3 numeros (osea son de tamaño 3)
#La ultima lista siempre tendrá tamaño (m-1)*k (osea tiene (m-1)* k escenas (las escenas son de tamaño 3))
#O((m-1)*k* 3), que es lineal en función de la cantidad total de números en las partes.

def comprimir(listaDePartes, m, k):
    numeros = []
    # Recorrer las primeras m-1 listas que son las primeras partes
    for i in range(m-1):
        parte = listaDePartes[i]
        for escena in parte:
            numeros.extend(escena)

    # Recorrer la última lista que representa la apertura
    ultima_parte = listaDePartes[-1]
    for i in range((m-1)*k):
        escena = ultima_parte[i]
        numeros.extend(escena)
    return numeros
"""
             m= cant de partes
             m-1=partes sin apertura
             k=cant de escenas en cada parte 
             (m-1)*k 
             cada escena siempre tiene 3 animes
"""
#complejidad O(n)
#retorna el numero que más se repide en una lista
def max(lista):
    frecuencia = {}
    max_frecuencia = 0
    moda = []
    for numero in lista:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
        if frecuencia[numero] > max_frecuencia:
            max_frecuencia = frecuencia[numero]
            moda = [numero]
        elif frecuencia[numero] == max_frecuencia:
            moda.append(numero)
    return moda, max_frecuencia

def minimo(lista):
    frecuencia = {}
    min_frecuencia = float('inf')
    moda_min = []

    for numero in lista:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1

    for numero, freq in frecuencia.items():
        if freq < min_frecuencia:
            min_frecuencia = freq
            moda_min = [numero]
        elif freq == min_frecuencia:
            moda_min.append(numero)

    return moda_min, min_frecuencia

def animalMasYmenosRepetido(apertura, partes, m, k):
   aperturaLen=(m-1)*k
   partesLen=m-1
   parteLen=k
   nuevalista=[]
   partes.append(apertura)
  # print("lista convinada: " ,  partes , len(partes))
   partes=comprimir(partes, m, k)
   #print("lista comprimida: ", partes , len(partes))
   return max(partes),  minimo(partes)

#print(animalMasYmenosRepetido(apertura, partes , 4, 3))


#Escena de menor y mayor grandeza. la apertura tiene todas las escenas entonces podemos buscarla ahí
def escenaDeMenorYmayorGrandeza(apertura):
    menor_grandeza = float('inf')
    mayor_grandeza = float('-inf')
    escena_menor_grandeza = None
    escena_mayor_grandeza = None

    for escena in apertura:
        grandeza = grandezaEscena(escena)
        if grandeza < menor_grandeza:
            menor_grandeza = grandeza
            escena_menor_grandeza = escena
        if grandeza > mayor_grandeza:
            mayor_grandeza = grandeza
            escena_mayor_grandeza = escena

    return escena_menor_grandeza, menor_grandeza, escena_mayor_grandeza, mayor_grandeza

def promedioGrandezaEspectaculo(apertura, partes):
    total_grandezas = 0
    total_escenas = 0
    # Calcular la suma de las grandezas de las escenas en la apertura
    for escena in apertura:
        total_grandezas += grandezaEscena(escena)
        total_escenas += 1
    # Calcular la suma de las grandezas de las escenas en las partes
    for parte in partes:
        for escena in parte:
            total_grandezas += grandezaEscena(escena)
            total_escenas += 1
    # Calcular el promedio de grandeza
    promedio = total_grandezas / total_escenas
    return promedio

#retorna los resultados del el espectaculo completo
def espectaculo(m, k, apertura, partes):
    return ordenarApertura(apertura, m, k), ordenarListaDePartes(partes, m ,k), animalMasYmenosRepetido(apertura, partes, m, k), escenaDeMenorYmayorGrandeza(apertura), promedioGrandezaEspectaculo(apertura, partes)

print(espectaculo(4,3, apertura, partes))



def visualizarResultado( resultado ):
    return resultado[0]
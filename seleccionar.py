
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
partes2=[parte1,parte2,parte3,apertura]

#Complejidad: O((m-1) * k^2)
def comprimir(listaDePartes, m, k):
    numeros = []
    # Recorrer las primeras m-1 listas que son las primeras partes
    #O((m-1) * k) * O(k) = O((m-1) * k^2)
    for i in range(m-1):
        parte = listaDePartes[i]
        for escena in parte:
            numeros.extend(escena) #O(k)

    # Recorrer la última lista que representa la apertura
    ultima_parte = listaDePartes[-1]
    #O((m-1) * k) * O(k) = O((m-1) * k^2)
    for i in range((m-1)*k):
        escena = ultima_parte[i]
        numeros.extend(escena)
    return numeros

#encuentra el maximo de una lista
#O(n), depende del tamaño de la lista
def maximo(lista):
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

#encuentra el minimo de una lista

#O(n), depende del tamaño de la lista
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

# O((m-1) * k^2) dominada por la funcion de comprimir
def animalMasYmenosRepetido(apertura, partes, m, k):
   #crear la copia tiene complejidad:
   aperturaAux=apertura[:] #O((m-1)*k)
   partesAux=partes[:] #O(k)
   partesAux.append(aperturaAux) #O(1)
  # print("lista convinada: " ,  partes , len(partes))
   partesAux=comprimir(partesAux, m, k) # O((m-1) * k^2)
  # print("lista comprimida: ", partesAux , len(partesAux))
   return maximo(partesAux), minimo(partesAux)

#Escena de menor y mayor grandeza. la apertura tiene todas las escenas entonces podemos buscarla ahí
#O(n)
def escenaDeMenorYmayorGrandeza(apertura):
    #O(1)
    menor_grandeza = float('inf')
    mayor_grandeza = float('-inf')
    escenas_menor_grandeza = []
    escenas_mayor_grandeza = []
    #O(n), n tamaño de apertura
    for escena in apertura:
        grand = grandeza.escena(escena)
        if grand < menor_grandeza:
            menor_grandeza = grand
            escenas_menor_grandeza = [escena]
        elif grand == menor_grandeza:
            escenas_menor_grandeza.append(escena)
        if grand > mayor_grandeza:
            mayor_grandeza = grand
            escenas_mayor_grandeza = [escena]
        elif grand == mayor_grandeza:
            escenas_mayor_grandeza.append(escena)
    
    return (escenas_menor_grandeza, menor_grandeza), (escenas_mayor_grandeza, mayor_grandeza)
#O(n + m)
def promedioGrandezaEspectaculo(apertura, partes):
    total_grandezas = 0
    total_escenas = 0
    # Calcular la suma de las grandezas de las escenas en la apertura
    for escena in apertura:
        total_grandezas += grandeza.escena(escena)
        total_escenas += 1
    # Calcular la suma de las grandezas de las escenas en las partes
    for parte in partes:
        for escena in parte:
            total_grandezas += grandeza.escena(escena)
            total_escenas += 1
    # Calcular el promedio de grandeza
    promedio = total_grandezas / total_escenas
    return promedio

#PRUEBAS:

#print("antes", partes, len(partes))
#print(animalMasYmenosRepetido(apertura, partes,m,k ))
#print("desp", partes, len(partes))





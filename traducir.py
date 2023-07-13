#Para hacer pruebas:
n = 9
m = 4
k = 3

animales = ["capibara", "loro", "caiman", "boa", "cocodrilo", "cebra", "pantera negra", "tigre", "leon"]
grandezas = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
apertura=[["caiman","capibara","loro"], ["boa","caiman","capibara"], ["cocodrilo","capibara","loro"], 
           ["pantera negra","cocodrilo","loro"], ["tigre","loro","capibara"], ["leon","caiman","loro"], 
           ["leon","cocodrilo","boa"], ["leon","pantera negra","cebra"], ["tigre","cebra","pantera negra"]]
parte1=[["caiman","capibara","loro"],["tigre","loro","capibara"], ["tigre","cebra","pantera negra"]]
parte2=[["pantera negra","cocodrilo","loro"], ["leon","pantera negra","cebra"], ["cocodrilo","capibara","loro"]]
parte3=[["boa","caiman","capibara"], ["leon","caiman","loro"], ["leon","cocodrilo","boa"]]
partes=[parte1,parte2,parte3]

"""
  m= cant de partes
  m-1=partes sin apertura
  k=cant de escenas en cada parte 
  (m-1)*k 
  cada escena siempre tiene 3 animes
"""
#complejidad O(n), con respecto a la cantidad de animales
def numeroToAnimal(animales, grandezas, grandeza):
    animal_index = grandezas.index(grandeza)
    animal = animales[animal_index]
    return animal

#complejidad O(n*tamañolista), lineal con respecto al tamaño de la lista
def lista(animales, grandezas, numeros, tamañoLista):
    listaTraducida = []
    for i in range(tamañoLista):
        numero = numeros[i]
        animal = numeroToAnimal(animales, grandezas, numero)
        listaTraducida.append(animal)
    texto = ", ".join(listaTraducida)
    return texto

#complejidad O(1), constante
def escenaToAnimal(animales, grandezas, escena):
    #las escenas tienen tamaño 3 siempre
    escenaTraducida = [
        numeroToAnimal(animales, grandezas, escena[0]),
        numeroToAnimal(animales, grandezas, escena[1]),
        numeroToAnimal(animales, grandezas, escena[2])
    ]
    return escenaTraducida

#complejidad O(k), lineal con respecto a K
def parteToAnimal(animales, grandezas, parte, k):
    #recuerde que k es el numero de escenas que tiene la parte a traducir
    parteTraducida = []
    for i in range(k):
        escena = parte[i]
        escenaTraducida = escenaToAnimal(animales, grandezas, escena) #complejidad O(1) 
        parteTraducida.append(escenaTraducida)
    return parteTraducida

#Complejidad O(m * k), lineal  con respecto al número de escenas.
def listaDePartesToAnimal(animales, grandezas, listaDePartes, m, k):
    #recuerde que m es el tamaño del arreglo de partes
    m=m-1
    listaTraducida = []
    for i in range(m):
        parteTraducida = parteToAnimal(animales, grandezas, listaDePartes[i], k)
        listaTraducida.append(parteTraducida)
    return listaTraducida

###################################################################################################

#complejidad O(n), con respecto a la cantidad de animales
def animalToGrandeza(animales, grandezas, animal):
    animal_index = animales.index(animal)
    grandeza = grandezas[animal_index]
    return grandeza

#complejidad O(1), constante porque la escena siempre tendrá tamaño 3
def EscenaToGrandeza(animales, grandezas, escena):
    escenaTraducida = [
        animalToGrandeza(animales, grandezas, animal)
        for animal in escena
    ]
    return escenaTraducida

#O(k*n) lineal con respecto a k
def parteToGrandeza(animales, grandezas, parte, k):
    parteTraducida = []
    for i in range(k):
        escena = parte[i]
        escenaTraducida = EscenaToGrandeza(animales, grandezas, escena)
        parteTraducida.append(escenaTraducida)
    return parteTraducida

#Complejidad O(m * k), lineal  con respecto al número de escenas.
def listaDePartesToGrandeza(animales, grandezas, listaDePartes, m, k):
    m=m-1
    listaTraducida = []
    for i in range(m):
        parteTraducida = parteToGrandeza(animales, grandezas, listaDePartes[i], k)
        listaTraducida.append(parteTraducida)
    return listaTraducida

#PRUEBAS:
"""
print(lista(animales, grandezas, [1], 1 ))
print("Parte1=",parteToGrandeza(animales, grandezas,parte1, k))
print("Parte1=",parteToGrandeza(animales, grandezas,parte2, k))
print("Parte1=",parteToGrandeza(animales, grandezas,parte3, k))
print("apertura=", parteToGrandeza(animales, grandezas, apertura, (m-1)*k))
print("apertura= ", parteToAnimal( animales, grandezas, parteToGrandeza(animales, grandezas, apertura, (m-1)*k), (m-1)*k))
print("Partes= ", listaDePartesToGrandeza(animales, grandezas,partes, m, k))
print("Partes= ", listaDePartesToAnimal(animales, grandezas, listaDePartesToGrandeza(animales, grandezas,partes, m, k), m, k))
"""


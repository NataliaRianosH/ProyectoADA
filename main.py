import algoritmosOrden

"""
#funcion: transformarArreglo
#parametros: arreglo: el arreglo sea de numeros,
             animales: diccionario que contiene los animales con sus respectivas grandezas
             opcion: 'animal' transforma de animales a numeros
                     'numero' transforma de numeros a animales
#complejidad: O(n*m) donde n=cantidadDeSubarreglos(tamaño del arreglo), 
                     m=tamañanoDeSubarreglo
                     como los subarreglos siempre serán de tamaño 3 (porque cada escena tiene 3 animales)
                     concluimos que la complejidad solo depende de n.
                     es decir O(n)
"""
def transformarArreglo(arreglo, animales, opcion):
    animal_dict = dict(animales)
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])): #siempre se ejecuta 3 veces, no importa el tamaño de la entrada
            elemento = arreglo[i][j]
            if opcion == 'animal' and elemento in animal_dict:
                arreglo[i][j] = animal_dict[elemento]
            elif opcion == 'numero':
                for key, value in animal_dict.items():
                    if value == elemento:
                        arreglo[i][j] = key
                        break
    return arreglo
#print(transformarArreglo([["gato","libelula","ciempies"]],[("gato", 3),("libelula", 2),("ciempies", 1),("nutria", 6),("perro", 4),("tapir", 5)],'animal'))
#print(transformarArreglo([[2,3,4],[3,4,5]],[("gato", 3),("libelula", 2),("ciempies", 1),("nutria", 6),("perro", 4),("tapir", 5)],'numero'))


"""
#Funcion: sumaEscena(parte) -> retorna una lista con la suma los elementos de las escenas
#Parametros: parte: una parte es una lista que se compone de escenas
#complejidad: todas las escenas son de tamaño 3, por lo que la complejidad depende
              de la cantidad de escenas que hay en la lista "parte", 
              es decir O(n)
"""
def sumaEscena(listaDeEscenas):
   totalSumas=[]
   for escena in listaDeEscenas:
      totalSumas.append(sum(escena))
   return totalSumas  
#print(sumaEscena([[1,2,3], [1,2,3]])) #[6,6]

"""
#funcion: sumasTotales(listaDePartes)-> lista con la grandeza total de cada parte
#parametros: listaDeParte: Es la lista que contiene todas las partes del acto, cada una de estas partes
             está consituida por escenas de tamaño 3.
#complejidad: O(n) la complejidad solo depende del tamaño de la listaDePartes              
"""
def sumasTotales(listaDePartes):
    sumatorias = []
    for parte in listaDePartes:
        sumaParte = sum(sumaEscena(parte)) 
        sumatorias.append(sumaParte)
    return sumatorias  
#print(sumasTotales([ [[1,2,3],[2,3,4]] , [[1,2,3]] ])) #[15,6]

"""
#funcion: animalMasRepetido(apertura, partes)-> el animal que más se repite teniendo en cuenta apertura y partes
#parametros: apertura: Lista que contiene la apertura
             partes: Lista que contiene las partes
#complejidad: O(n)
"""
def animalMasRepetido(apertura, partes):
    conteo_animales = {}

    def contar_animales(escenas):
        for escena in escenas:
            for animal in escena:
                if animal in conteo_animales:
                    conteo_animales[animal] += 1
                else:
                    conteo_animales[animal] = 1

    contar_animales(apertura)

    for parte in partes:
        contar_animales(parte)

    max_repeticiones = max(conteo_animales.values())
    animales_mas_repetidos = [animal for animal, repeticiones in conteo_animales.items() if repeticiones == max_repeticiones]

    return animales_mas_repetidos, max_repeticiones

print(animalMasRepetido([[1,2,3]], [ [[1,2,3], [1,2,6]], [[4,3,6]]]))
"""
lo mismo anterior solo que selecciona el que menos se repite
"""
def animalMenosRepetido(apertura, partes):
    conteo_animales = {}

    def contar_animales(escenas):
        for escena in escenas:
            for animal in escena:
                if animal in conteo_animales:
                    conteo_animales[animal] += 1
                else:
                    conteo_animales[animal] = 1

    contar_animales(apertura)

    for parte in partes:
        contar_animales(parte)

    min_repeticiones = min(conteo_animales.values())
    animales_menos_repetidos = [animal for animal, repeticiones in conteo_animales.items() if repeticiones == min_repeticiones]

    return animales_menos_repetidos, min_repeticiones

#print(animalMenosRepetido([[1,2,3]], [ [[1,2,3], [1,2,6]], [[4,3,6]]]))



"""
#funcion: espectaculo
#parametros: n=cant de animales
             m= cant de partes, sin la apertira
             k=cant de escenas en cada parte 
             cada escena siempre tiene 3 animes
"""
def espectaculo(n,m,k,animales,apertura,partes):
    
    #pasar animales de apertura a numeros
    transformarArreglo(apertura,animales,'animal')
    #pasar aniamles del arreglo partes a numeros
    for parte in partes:
       transformarArreglo(parte,animales,'animal')
    
    #Ordenar escenas de apertura de acuerdo a la suma de grandezas de cada escena
    sumasDeEscenas= sumaEscena(apertura)
    algoritmosOrden.insertion_sort(apertura,sumasDeEscenas)
    #Ordenar elementos en cada escena de la apertura
    for escenaApertura in apertura:
        algoritmosOrden.insertion_sort(escenaApertura,escenaApertura)

    #Ordenar escenas en cada parte de acuerdo a la suma de grandezas
    for parteA in partes:
         algoritmosOrden.insertion_sort(parteA,sumaEscena(parteA))
    #Ordenar elementos en cada escena de cada parte
    for i in partes:
        for elem in i:
            algoritmosOrden.insertion_sort(elem,elem)
    #ordenar listado de partes de acuerdo a sumas totales

    algoritmosOrden.insertion_sort(partes,sumasTotales(partes))           

    #pasar valores de apertura a animales
    transformarArreglo(apertura,animales,'numero')
    #pasar valores de partes a animales
    for elemento in partes:
        transformarArreglo(elemento,animales,'numero')

    imprimir(apertura,partes,sumasDeEscenas)         
    return 

def imprimir(apertura,partes,sumas):
    print('El orden en el que se debe presentar el espectaculo es:\nApertura: ', apertura)
    conta=0
    for parte in partes:
      conta+=1
      print('\nParte',conta,': ', parte)
    promedio= sum(sumas)/len(sumas)
    
    #primero debemos ordenar el arreglo de sumas para que el indice
    algoritmosOrden.insertion_sort(sumas,sumas)
    #hallar menor y mayor escena
    menor = sumas[0]
    mayor= sumas[0]
    for j in range(1, len(sumas)):
        if sumas[j]< menor:
           menor= sumas[j]
        else:
           mayor= sumas[j]   
    menor= apertura[sumas.index(menor)]
    mayor= apertura[sumas.index(mayor)]
    print("la apertura es: ", apertura)
    masRepetidos, max = animalMasRepetido(apertura, partes)
    print("\nEl animal que participo en mas escenas dentro del espectaculo fue", ", ".join(masRepetidos), "con", max, "escenas.")
    
    menosRepetidos, min = animalMenosRepetido(apertura, partes)
    print("\nEl animal que participo en menos escenas dentro del espectaculo fue", ", ".join(menosRepetidos), "con", min, "escenas.")

    print('\nLa escena de menor grandeza total fue la escena ',menor)
    print('\nLa escena de mayor grandeza total fue la escena',mayor)        
    print('\nEl promedio de grandeza de todo el espectaculo fue de: ',promedio)
    return

#espectaculo(n,m,k,animales,apertura,partes)
"""
def masRepetido(lista):
    contador = {}
    max_repetido = 0
    
    for numero in lista:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
        
        if contador[numero] > max_repetido:
            max_repetido = contador[numero]
    
    numeros_repetidos = [numero for numero, count in contador.items() if count == max_repetido]
    
    if len(numeros_repetidos) == 1:
        return numeros_repetidos[0], max_repetido
    else:
        return numeros_repetidos, max_repetido
def animalMasRepetido(apertura, partes):
    todas_las_escenas = apertura + partes
    todos_los_numeros = []
    for escena in todas_las_escenas:
        for numero in escena:
            todos_los_numeros.append(numero)
    return masRepetido(todos_los_numeros)
    print(masRepetido([1, 2, 3, 1, 2, 3, 1, 2, 6, 4, 3, 6]))  # ([1, 2, 3], 3)


    
"""

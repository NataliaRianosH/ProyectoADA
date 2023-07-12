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
                     es decir O

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

    print("n=", n, "m=", m, "k= ", k)
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

    masRepetidos, max = animalMasRepetido(apertura, partes)
    print("\nEl animal que participo en mas escenas dentro del espectaculo fue", ", ".join(masRepetidos), "con", max, "escenas.")
    
    menosRepetidos, min = animalMenosRepetido(apertura, partes)
    print("\nEl animal que participo en menos escenas dentro del espectaculo fue", ", ".join(menosRepetidos), "con", min, "escenas.")

    print('\nLa escena de menor grandeza total fue la escena ',menor)
    print('\nLa escena de mayor grandeza total fue la escena',mayor)        
    print('\nEl promedio de grandeza de todo el espectaculo fue de: ',promedio)
    return

#[15, 12, 9, 6]
#sumas de cada escena
def sumaEscena(A):
   totalSumas=[]
   for escena in A:
      totalSumas.append(sum(escena))
   return totalSumas   

#[[24],[18]]
#suma total de cada parte
def sumasTotales(A):
  sumatorias=[]
  for parte in A:
    suma=[]
    for escena in parte:
      suma.append(sum(escena))
    sumaParte= sum(suma)
    sumatorias.append(sumaParte)
  return sumatorias  


#espectaculo(n,m,k,animales,apertura,partes)

def animalMasRepetido(apertura, partes):
    conteo_animales = {}

    # Contar la cantidad de veces que aparece cada animal en la apertura
    for escena in apertura:
        for animal in escena:
            if animal in conteo_animales:
                conteo_animales[animal] += 1
            else:
                conteo_animales[animal] = 1

    # Contar la cantidad de veces que aparece cada animal en las partes
    for parte in partes:
        for escena in parte:
            for animal in escena:
                if animal in conteo_animales:
                    conteo_animales[animal] += 1
                else:
                    conteo_animales[animal] = 1

    # Encontrar la cantidad máxima de repeticiones
    max_repeticiones = max(conteo_animales.values())

    # Obtener los animales con la cantidad máxima de repeticiones
    animales_mas_repetidos = [animal for animal, repeticiones in conteo_animales.items() if repeticiones == max_repeticiones]

    return animales_mas_repetidos, max_repeticiones

def animalMenosRepetido(apertura, partes):
    conteo_animales = {}

    # Contar la cantidad de veces que aparece cada animal en la apertura
    for escena in apertura:
        for animal in escena:
            if animal in conteo_animales:
                conteo_animales[animal] += 1
            else:
                conteo_animales[animal] = 1

    # Contar la cantidad de veces que aparece cada animal en las partes
    for parte in partes:
        for escena in parte:
            for animal in escena:
                if animal in conteo_animales:
                    conteo_animales[animal] += 1
                else:
                    conteo_animales[animal] = 1

    # Encontrar la cantidad mínima de repeticiones
    min_repeticiones = min(conteo_animales.values())

    # Obtener los animales con la cantidad mínima de repeticiones
    animales_menos_repetidos = [animal for animal, repeticiones in conteo_animales.items() if repeticiones == min_repeticiones]

    return animales_menos_repetidos, min_repeticiones

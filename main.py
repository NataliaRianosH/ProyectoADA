import algoritmosOrden
n = 6

m = 3

k = 2

animales = [
    ("ciempies", 1),
    ("libelula", 2),
    ("gato", 3),
    ("perro", 4),
    ("tapir", 5),
    ("nutria", 6)
]

apertura = [["tapir", "nutria", "perro"], ["tapir", "perro", "gato"], ["ciempies", "tapir", "gato"], ["gato", "ciempies", "libelula"]]

partes = [[['tapir', 'nutria', 'perro'],['ciempies', 'tapir', 'gato']],
           [['gato', 'ciempies', 'libelula'],['tapir', 'perro', 'gato']]
         ]

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

def imprimir(A,B,sumas):
    print('El orden en el que se debe presentar el espectaculo es:\nApertura: ', A)
    conta=0
    for parte in B:
      conta+=1
      print('\nParte',conta,': ', parte)
    promedio=  sum(sumas)/len(sumas)
    
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
    menor= A[sumas.index(menor)]
    mayor= A[sumas.index(mayor)]

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

#Pasar el arreglo de animales a numeros o viceversa
def transformarArreglo(A,animales,opcion):
    for i in range(len(A)):
      for j in range(len(A[i])):
        elemento = A[i][j]
        for animal in animales:
            if opcion == 'animal' and animal[0] == elemento:
                A[i][j] = animal[1]
                break
            elif opcion == 'numero' and animal[1] == elemento:
                A[i][j] = animal[0]
                break


#espectaculo(n,m,k,animales,apertura,partes)
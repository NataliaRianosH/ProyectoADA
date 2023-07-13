import traducir 
import ordenar 
import seleccionar 
import time
#Para hacer pruebas:
n = 9
m = 4
k = 3
"""
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
#FUNCIONES PARA TRADUCIR DE NUMERO A ANIMAL:

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

 
def espectaculo(n, m, k, animales, grandezas, apertura, partes):
   start_time = time.time()
   aperturaLen=(m-1)*k
   partesLen=m-1
   parteLen=k
   escenasLen=3

   #traducir entradas:
   apertura=traducir.parteToGrandeza(animales, grandezas, apertura, (m-1)*k)
   partes=traducir.listaDePartesToGrandeza(animales, grandezas , partes, m, k)

   #ordenar:
   ordenar.parte(apertura, (m-1)*k)
   #imprimir
   print("El orden en el que se debe presentar el espectaculo es")
   print("Apertura= ", traducir.parteToAnimal(animales, grandezas,apertura,(m-1)*k))
   
   #ordenar las partes:
   ordenar.listaDePartes(partes, m, k)
   for i in range(m-1):
     print("Parte", i+1, "= ", traducir.parteToAnimal(animales, grandezas, partes[i], k))
    
   #animales
   animalQueMasParticipo , animalQueMenosParticipo = seleccionar.animalMasYmenosRepetido(apertura, partes,m,k)
   print("El animal que participo en mas escenas dentro del espectaculo fue", traducir.lista(animales, grandezas, animalQueMasParticipo[0], len(animalQueMasParticipo[0])), " con ", animalQueMasParticipo[1], " escenas" )
   print("El animal que participo en menos escenas dentro del espectaculo fue", traducir.lista(animales, grandezas, animalQueMenosParticipo[0], len(animalQueMenosParticipo[0])), " con ", animalQueMenosParticipo[1], " escenas" )
   
   #escenas:
   escenaGrandezaMenor, escenaGrandezaMayor = seleccionar.escenaDeMenorYmayorGrandeza(apertura)
   print("La escena de menor grandeza total fue la escena", traducir.parteToAnimal(animales, grandezas, escenaGrandezaMenor[0], len(escenaGrandezaMenor[0])), " con grandeza =", escenaGrandezaMenor[1])
   print("La escena de mayor grandeza total fue la escena", traducir.parteToAnimal(animales, grandezas, escenaGrandezaMayor[0], len(escenaGrandezaMayor[0] )), " con grandeza =", escenaGrandezaMayor[1])
   #El promedio de grandeza de todo el espectaculo fue de 

   print("El promedio de grandeza de todo el espectaculo fue de ", seleccionar.promedioGrandezaEspectaculo(apertura, partes))
   end_time = time.time()
   return end_time - start_time 

#espectaculo(n, m, k, animales, grandezas, apertura, partes)
   
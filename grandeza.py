# Funciones para determinar la grandeza total. Complejidad constante 

"""
#funcion escena(escena)-> grandeza de una escena
#parametros: escena: es una lista de 3 numeros, cada numero representa la grandeza de un animal
#objetivo: calcular la grandeza total de una escena. La grandeza total de una escena es igual a
           sumar las grandezas de cada animal que la compone
#complejidad: O(1), las escena siempre tendran 
"""
def escena(escena):
   return escena[0]+ escena[1]+ escena[2]
"""
#funcion parte(parte)-> grandeza de una parte
#parametros: parte: es una lista con formada de k escenas
#            k: cantidad de escenas en la parte
#objetivo: calcular la grandeza total de una parte. la grandeza total de una parte es
           igual a la suma de las grandezas 
#complejidad: O(k), constante con respecto a k
"""
def parte(parte, k):
   suma_grandezas = 0
   for i in range(k):
       suma_grandezas += escena(parte[i])
   return suma_grandezas

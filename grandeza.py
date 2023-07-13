
def escena(escena):
   return escena[0]+ escena[1]+ escena[2]

def parte(parte, k):
   suma_grandezas = 0
   for i in range(k):
       suma_grandezas += escena(parte[i])
   return suma_grandezas

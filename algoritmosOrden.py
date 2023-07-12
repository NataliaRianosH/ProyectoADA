#algoritmo para ordenar de acuerdo a la sumatoria de cada escena (cuando opcion es igual a 'suma'), de acuerdo a los elementos del arreglo (cuando opcion es igual a 'valor'), ordenar cada parte de acuerdo a la suma total de la escena (cuando opcion es igual a total)
# def insertion_sort(A,opcion):
#     for j in range(1, len(A)):
#         key = A[j]
#         i = j - 1
#         if (opcion =='suma'):
#           while i >= 0 and sum(A[i]) > sum(key):
#               A[i + 1] = A[i]
#               i = i - 1
#           A[i + 1] = key
#         elif (opcion == 'valor'):       
#           while i >= 0 and A[i]> key:
#             A[i + 1] = A[i]
#             i = i - 1
#           A[i + 1] = key
#         elif (opcion == 'total'):
#           sumaPartes= sumasTotales(A)
#           while i >= 0 and sumaPartes[i]> sumaPartes[j]:
#             A[i + 1] = A[i]
#             i = i - 1
#           A[i + 1] = key
             
def insertion_sort(A,arregloGuia):
    for j in range(1, len(A)):
        key = arregloGuia[j]
        new= A[j]
        i = j - 1
        while i >= 0 and arregloGuia[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = new

        
           












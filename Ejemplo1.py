import solucion as solucion
import traducir as traducir
#EJEMPLO 1 DEL ENUNCIADO
n = 6
m = 3
k = 2

animales = [ "ciempies", "libelula","gato", "perro", "tapir", "nutria"]
grandezas= [1,2,3,4,5,6]

apertura= [["tapir", "nutria", "perro"], ["tapir", "perro", "gato"], ["ciempies", "tapir", "gato"], ["gato", "ciempies", "libelula"]]
parte1= [["tapir", "nutria", "perro"], ["ciempies", "tapir", "gato"]]
parte2= [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]

partes = [parte1, parte2]

solucion.espectaculo(n, m, k, animales, grandezas, apertura, partes)
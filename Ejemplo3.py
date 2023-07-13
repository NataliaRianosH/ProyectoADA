import solucion
#ejemplo input1
n = 6
m = 3
k = 2

animales = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
grandezas = [3, 2, 1, 6, 4, 5]

apertura = [["tapir", "nutria", "perro"], ["tapir", "perro", "gato"], ["ciempies", "tapir", "gato"],
            ["gato", "ciempies", "libelula"]]

parte1 = [["tapir", "nutria", "perro"], ["ciempies", "tapir", "gato"]]
parte2 = [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]

partes = [parte1, parte2]

solucion.espectaculo(n, m, k, animales, grandezas, apertura, partes)

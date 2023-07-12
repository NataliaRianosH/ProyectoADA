import main
#EJEMPLO INPUT1
n = 6

m = 3

k = 2

animales = [
    ("gato", 3),
    ("libelula", 2),
    ("ciempies", 1),
    ("nutria", 6),
    ("perro", 4),
    ("tapir", 5)
]

apertura = [["tapir", "nutria", "perro"], ["tapir", "perro", "gato"], ["ciempies", "tapir", "gato"], ["gato", "ciempies", "libelula"]]

partes = [[['tapir', 'nutria', 'perro'],['ciempies', 'tapir', 'gato']],
           [['gato', 'ciempies', 'libelula'],['tapir', 'perro', 'gato']]
         ]

main.espectaculo(n,m,k,animales,apertura,partes)

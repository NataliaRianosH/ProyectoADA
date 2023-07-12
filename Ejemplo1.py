import main
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

main.espectaculo(n,m,k,animales,apertura,partes)

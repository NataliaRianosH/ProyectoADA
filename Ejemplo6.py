import main 
import time

inicio = time.time()

n = 30
m = 3
k = 9

animales = [
    ("mono", 5),
    ("araña", 1),
    ("rinoceronte", 7),
    ("elefante", 9),
    ("perico", 3),
]

apertura = [["mono","araña","rinoceronte"], ["araña","rinoceronte","elefante"], ["rinoceronte","elefante","perico"], 
           ["perico","mono","araña"], ["rinoceronte","elefante","mono"], ["araña","elefante","perico"], 
           ["elefante","mono","perico"], ["elefante","rinoceronte","mono"], ["mono","araña","elefante"],
           ["mono","perico","rinoceronte"], ["perico","araña","elefante"], ["perico","araña","rinoceronte"]]

parte1=[["mono","araña","rinoceronte"],["rinoceronte","elefante","mono"], ["mono","araña","elefante"]]
parte2=[["mono","perico","rinoceronte"], ["elefante","rinoceronte","mono"], ["araña","elefante","perico"]]
partes = [parte1, parte2]

main.espectaculo(n,m,k,animales,apertura,partes)

final = time.time()
print (final-inicio)
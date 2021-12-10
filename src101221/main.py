import libs.infosistema as lib
import math

# Modulo esterno
lib.info()

print()
# Esempio uso cmath
print(math.sin(math.degrees(45)))

print()
# Variabili
lista = [
    {"nome": "uno", "eta": 1},
    {"nome": "due", "eta": 2},
    {"nome": "tre", "eta": 3}
]
for i in range(len(lista)):
    print("Nome %s, di età %s" % (lista[i]["nome"], lista[i]["eta"]))
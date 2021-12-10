import libs.infosistema as lib
from libs.liste import crea_lista
import math

# Modulo esterno
lib.info()

print()
# Esempio uso cmath
print(math.sin(math.degrees(45)))

print()
# Variabili
n_elementi = input("Inserire il numero di elementi della lista: ")
lista_test = [
    {"nome": "uno", "eta": 1},
    {"nome": "due", "eta": 2},
    {"nome": "tre", "eta": 3}
]
lista = crea_lista(int(n_elementi))
for i in range(len(lista)):
    print("Nome %s, di età %s" % (lista[i]["nome"], lista[i]["eta"]))
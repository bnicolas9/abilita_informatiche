import libs.listmod as listmod
import libs.lib2 as lib
from time import perf_counter as time

#=============================================

M = int(input("Numero massimo: "))
a = listmod.prodottocartesiano(M, False)

t0 = time()
a + a
print("Somma: ", str(time() - t0))

t0 = time()
a.extend(a)
print("Extend: ", str(time() - t0))

#=============================================

print("\nListe:")
b = [i for i in range(0,10)]
print("Inizio processo. Lista = " + str(b))
for i in range(0, 10):
    t = b[0]
    b.pop(0)
    print("Elemento: " + str(t))
    print(b)
print("Fine processo. Lista = " + str(b))

#=============================================

print("\nTuple:")
tp = ("test", 4, 5, False)
for element in tp:
    print(element)

#=============================================

print("\nFor con break")
for i in range(0, 5):
    print("For: ", i)
    if i == 3:
        break
else:
    print("Else")

print("\nFor senza break")
for i in range(0, 5):
    print("For: ", i)
else:
    print("Else")
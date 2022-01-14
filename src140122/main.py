#import sys
import numpy as np
import random
import lib

nmax = input("- Inserisci numero massimo: ") #if len(sys.argv) < 1 else sys.argv[0]

fill = int(nmax) / 2
m = [ [random.randint(0, int(fill)) for j in range(0, int(nmax))] for i in range(0, int(nmax))]

open("./src140122/test.txt", "w").close()
with open("./src140122/test.txt", "w") as f:
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if j == len(m) - 1:
                f.write(str(m[i][j]))
            else:    
                f.write(str(m[i][j]) + ",")
        f.write("\n")

m2 = np.loadtxt("./src140122/test.txt", delimiter=",", dtype="i")
print(m2)

print("\n- Moltiplicazione per uno scalare:")
print(2 * m2)

print("\n- Moltiplicazione per matrice:")
print(np.dot(m2, m2))
print("    oppure esplicitamente:")
r = []
for i in range(0, len(m2)):
    r.append([0 for i in range(0, len(m2))])
    for j in range(0, len(m2)):
        for k in range(0, len(m2)):
            r[i][j] += m2[i][k] * m2[k][j]
print(np.matrix(r))

#===================================================

print()
test = lib.Shape("parallelogramma", [[2,0], [5,5]])
print("Area parallelogramma: ", test.area())

#===================================================

print()
a = int(input("Inserisci dividendo: "))
b = int(input("Inserisci divisore: "))
try:
    c = lib.div(a, b)
    if c == 1:
        raise NameError("Identità")
except ZeroDivisionError:
    print("Divisione per zero")
else:
    print("Divisione riuscita")
finally:
    print("Indipendentemente, questo si scrive sempre")

#===================================================

print()
l1 = [i for i in range(0, 5)]
l2 = [i for i in range(5, 8)]
l3 = zip(l1, l2)
print(str(l1) + " +zip+ " + str(l2) + " = " + str(list(l3)))
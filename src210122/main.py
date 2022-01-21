def sign(x):
    from numpy import where
    return where(x > 0, "+", "-")

x = int(input("Inserisci numero: "))
print("Segno del numero inserito: ", sign(x))
def prodottocartesiano(M, s):
    X = [x for x in range(0,M)]
    Y = [y for y in range(0, M)]

    p = [(a, b) for a in X for b in Y]

    if s:
        print("1: ", X)
        print("2: ", Y)
        print("T: ", p)
        
    return p

def quadrati(n):
    a = {i : i ** 2 for i in range(20)}

    if n in a:
        return True
    else:
        return False
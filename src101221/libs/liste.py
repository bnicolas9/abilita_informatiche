def crea_lista(n):
    l = []
    for i in range(n):
        a = chr(65+i)
        l.append({"nome": a, "eta": i+1})
    return l
        
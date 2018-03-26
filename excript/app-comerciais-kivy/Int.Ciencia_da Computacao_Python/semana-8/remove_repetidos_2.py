def remove_repetidos(*lista):
    i = 0
    f = 0
    lista2 = []
    while f < len(lista):
        lista2.append(lista[f])
        f += 1
    while i < len(lista2):
        p = lista2[i]
        valor = lista2.count(p)
        if valor > 1:
            del(lista2[i])
        else:
            i += 1
    print(sorted(lista2))
remove_repetidos(1,2,3)
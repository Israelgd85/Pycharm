lista = [1,2,3,4,5,5,3]
def remove_repetidos(lista):
    i = 0
    while i < len(lista):
        p = lista[i]
        valor = lista.count(p)
        if valor > 1:
            del (lista[i])
        else:
            i += 1
    return(sorted(lista))
remove_repetidos(lista)
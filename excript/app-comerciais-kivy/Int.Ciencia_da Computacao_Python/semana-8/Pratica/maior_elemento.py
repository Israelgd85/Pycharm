lista = [12,5,6,7,8,20]
def maior_elemento(lista):
    i = 1
    maior = lista[0]
    while i < len(lista):
        if maior < lista[i]:
            maior = lista[i]
        else:
            i += 1
    return (maior)
maior_elemento(lista)
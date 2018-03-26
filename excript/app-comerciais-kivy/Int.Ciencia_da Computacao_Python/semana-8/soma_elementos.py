lista = [1,2,3,4,5,5,3]
def soma_elementos(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma = soma + lista[i]
        i += 1
    return(soma)
soma_elementos(lista)
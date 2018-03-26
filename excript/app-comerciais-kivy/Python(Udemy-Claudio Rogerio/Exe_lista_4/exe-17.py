#17) Escreva uma função que receba como argumento uma lista que poderá ter
#  valores duplicados e retorne uma nova lista sem que haja valores iguais.
#Lista: [1,2,3,3,3,3,4,5]
#Retorno: [1, 2, 3, 4, 5]

lista = [9,1,2,3,2,4,4,5,6,7,8,8]
def func_numeros_iguais(n):
    i = 0
    while i < len(lista):
        p = lista[i]
        valor = lista.count(lista[p])
        if valor > 1:
            del(lista[i])
        else:
            i += 1
    print(sorted(lista))
func_numeros_iguais(lista)





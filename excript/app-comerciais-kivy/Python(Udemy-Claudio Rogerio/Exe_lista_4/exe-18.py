# 18) Escreva uma função capaz de receber uma quantidade
#  indeterminada de parâmetros e imprima na telas os números
# primos contidos nessa lista.

#lista = [1,2,3,4,5,6,7,8,9,10]
def func_conver_list(*lista):
    i = 0
    cont = 1
    primos = []
    while cont < len(lista):
        mod = lista[i]
        if mod == 1:
            i += 1
            continue
        div = 0
        p = 1
        while p < len(lista):
            if mod % p == 0:
                div += 1
                p += 1
            else:
                p += 1
        if div ==2:
            primos.append(mod)
            cont += 1
            i += 1
        else:
            i += 1
            cont += 1
    print(primos)
func_conver_list(1,2,3,4,5,6,7,8,9,10)

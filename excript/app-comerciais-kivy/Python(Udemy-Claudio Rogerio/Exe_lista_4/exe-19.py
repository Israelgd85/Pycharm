# 19) Escreva uma função que imprima somente os números pares
#Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Saída: [2, 4, 6, 8]

def func_pares(*args):
    i = 0
    pares = []
    while i < len(args):
        n = args[i]
        if n % 2 == 0:
            pares.append(n)
            i += 1
        else:
            i += 1
    print(pares)
func_pares(1,2,3,4,5,6,7,8,9,10)
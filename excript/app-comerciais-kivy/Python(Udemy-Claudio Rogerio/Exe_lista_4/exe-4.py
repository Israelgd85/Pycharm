# 4) Escreva um algoritmo contendo uma função que necessite de três argumentos.
# Em seguida, imprima na tela os argumentos em ordem ascendente e,
# por fim, imprima a média aritmética:


arg = [23,13,12]

def ascendente (x,y,z):

    media = (x + y + z) / 3
    print(arg)
    print("A média caculada é :", media)

arg.sort()

ascendente(*arg)


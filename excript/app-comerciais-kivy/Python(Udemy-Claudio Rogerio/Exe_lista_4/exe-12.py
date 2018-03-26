# 12) Escreva uma função que multiplique todos os números de uma lista.
#Lista: (1, 2, 3, 4, 5)
#Multiplicação: 120

lista = (1,2,3,4,5)
def func_multiplica (a,b,c,d,e):
    total = a * b * c * d * e
    print(total)

func_multiplica(*lista)


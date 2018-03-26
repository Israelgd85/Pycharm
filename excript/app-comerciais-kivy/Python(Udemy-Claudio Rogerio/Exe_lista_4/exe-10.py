# 10) Escreva um algoritmo que encontre o maior dentre 3 números.
# Para facilitar a resolução do exercício utilize funções.

def func_maior_numero (a,b,c):
        if a > b and a > c:
            print(a)
        elif b > a and b > c:
            print(b)
        else:
            print(c)
func_maior_numero(3,4,1)
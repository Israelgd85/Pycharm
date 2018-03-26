#14) Escreva uma função que calcule o fatorial de um número (um inteiro não negativo).
# Envie o valor do número que será calcula como argumento da função.


n = int(input("Informe o numero para o calculo do fatorial: "))
def func_fatorial(n):
    fat = 1
    i = 1
    while n >= i :
        fat = fat * i
        i += 1
    print(fat)
func_fatorial(n)


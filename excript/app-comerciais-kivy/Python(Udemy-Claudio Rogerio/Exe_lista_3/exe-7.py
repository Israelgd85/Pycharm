# 7) Faça um algoritmo que calcule os número primos num intervalo pré-determinado
#  pelo usuário:


num1 =  int(input("Digite um intervalo para o calculo dos numeros primos: "))
print()
for i in range(2, num1):
    n = 0
    p = 0
    div = 0
    while p < num1:
        p += 1
        n += 1
        if (i % n == 0):
            div+=1
            continue
    if (div==2):
       print(i)
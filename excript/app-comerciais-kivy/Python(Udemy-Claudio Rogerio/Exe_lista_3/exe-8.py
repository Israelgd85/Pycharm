#8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário
# e permita que o mesmo possa definir 3 números que deverão ser ignorados,
# ou seja, que não serão impressos na tela:




num1 = int(input("Digite um intervalo para o calculo dos numeros primos: "))
print()
num2 = int(input("Digite o primeiro numero a ser ignorado: "))
num3 = int(input("Digite o segundo numero a ser ignorado: "))
num4 = int(input("Digite o terceiro numero a ser ignorado: "))

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
    if(num2==i or num3==i or num4==i):
        continue
    if (div==2):
       print(i)


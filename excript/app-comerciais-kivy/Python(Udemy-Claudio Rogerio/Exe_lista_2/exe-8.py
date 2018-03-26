#8) Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))



if num1 > num2:
    print(num1, "," ,num2)
else:
    print(num2, ",", num1)
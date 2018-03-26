#Básico I 1) Faça um algoritmo que solicite ao usuário digitar 2 números.
# Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

res1 = num1/num2


print("Total da divisão Decimal: ",res1 )
print("Total da Inteiro: %.0f  "%res1)
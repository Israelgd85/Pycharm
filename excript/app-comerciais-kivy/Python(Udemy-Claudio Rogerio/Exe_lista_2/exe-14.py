# 14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.


num1 = 30
num2 = 20
num3 = 50


if (num1>num2 and num1<num3 and num2>num3) :
    print(num1,num2,num3)
elif (num1 > num3 and num3 > num2 and num3 > num2):
    print(num1, num3, num2)
elif (num2 > num1 and num2 > num3 and num1 > num3):
    print(num2, num1, num3)
elif (num2 > num3 and num2 > num1 and num3 > num1):
    print(num2, num3, num1)
elif (num3 > num1 and num3 > num2 and num1 > num2):
    print(num3, num1, num2)
elif (num3 > num2 and num3 > num1 and num2 > num1):
    print(num3, num2, num1)


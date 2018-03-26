#Bloco de instrução Prática

num1 = int(input("Digite um numero: "))

a=5.0



if(num1>10):
    print("O valor é maior do que 10")
    if(num1<=15):
        print("O valor é maior do que 10, mas menor do que 15")
    else:
        if(num1<=50):
            print("O valor é maior do que 10, mas memor do que 50!")
        else:
            print("O valor é maior do que 50!")
else:
    if(num1>5):
        print("O numero é menor do que 10 mas maior do que 5")
        if(num1==7):
            print("O numero é igual a 7.")
    else:
        print("O valor é menor do que 5")

print(a)
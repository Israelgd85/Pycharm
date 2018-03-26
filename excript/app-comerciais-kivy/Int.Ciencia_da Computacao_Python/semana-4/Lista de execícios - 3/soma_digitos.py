a = int(input("Digite um número inteiro: "))
c = 0
while a != 0:
    b = a % 10
    a = a // 10
    c = c + b
print(c)
a = int(input("Digite um número inteiro: "))
c = b = a % 10
a = a // 10
adj = 0
while a > 0:
    b = a % 10
    a = a // 10
    d = b
    if c == d:
        print("Sim")
        break
    else:
        c = b
else:
    print("Não")






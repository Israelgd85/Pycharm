# n = int(input("Digite um número inteiro: "))
n = 0
while n >= 0:
    n = int(input("Digite um número inteiro: "))
    def fat(n):
        fatorial = 1
        while n > 1 and n > 0:
            fatorial = fatorial * n
            n = n - 1

        print(fatorial)


    fat(n)


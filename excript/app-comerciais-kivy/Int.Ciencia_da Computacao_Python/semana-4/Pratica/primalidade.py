num =  int(input("Digite um numero inteiro: "))
div = 0
n = 0
while n <= num :
    n += 1
    if num % n == 0:
        div += 1
        continue
if div == 2:
    print("Primo")
if div != 2:
    print("Não Primo")


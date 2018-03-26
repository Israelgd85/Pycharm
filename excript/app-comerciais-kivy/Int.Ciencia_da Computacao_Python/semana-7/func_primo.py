num = int(input("Iforme um numero inteiro: "))

def eprimo(num):
        n = 0
        p = 0
        div = 0
        while p <= num:
            p += 1
            n += 1
            if (num % n == 0):
                div += 1
                continue
        if (div == 2):
            return True
        else:
            return False
eprimo(num)

while num > 0:
    if eprimo(num):
        print("É primo")
    else:
        print("Não é primo")
    num = int(input("Iforme um numero inteiro: "))
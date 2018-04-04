try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Não é possivel dividir um numero por zero")
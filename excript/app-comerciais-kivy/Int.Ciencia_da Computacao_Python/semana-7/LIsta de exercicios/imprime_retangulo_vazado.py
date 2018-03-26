cl = int(input("Informe a largura do retangulo: "))
ln = int(input("Informe a altura do retangulo: "))
lt = ln
i = 0
n = 1
while ln >= n :
    ln = lt
    i = 2
    print("#", end="")
    while cl > i :
        if n == 1 or n == lt:
            print("#", end="")
            i += 1
        else:
            print(end = " ")
            i += 1
    print("#")
    n += 1
num = int(input("Informe um numeo inteiro: "))

def iverter (num):
    lista = []
    while num != 0:
        num = int(input("Informe um numeo inteiro ou 0 para sair: "))
        lista.append(num)
        if num == 0:
            del(lista[-1])
    lista2 = lista[::-1]
    print(lista2)
iverter(num)
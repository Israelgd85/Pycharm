#15) Escreva uma função que verifique se um número está num intervalo determinado.


#intervalo = int(input("Digite o intervalo: "))
num = int(input("Informe o numero: "))

def func_intervalo (n):
    for i in range (1,100,1):
        if num == i:
            print("O numero ", num, "esta no intervalo")
            return num
    else:
        print("O numero", num, "Não esta no intervalo")

func_intervalo(num)


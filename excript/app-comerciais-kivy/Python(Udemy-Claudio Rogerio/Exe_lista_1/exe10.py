# Basico I 10) Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:

num = int(input("Informe um numero a ser calculado: "))
op = int(input("Digite 1 para calcular o quadrado do numero ou 2 para calcular o cubo: "))



if(op==1):
    print("O quadrado do numero",num,"é: ",num**2)
elif(op==2):
    print("O cubo do",num,"é: ",num**3)
else:
    if(op!=1 or op!=2):
        print("Opção informada não é valida digite 1 ou 2")







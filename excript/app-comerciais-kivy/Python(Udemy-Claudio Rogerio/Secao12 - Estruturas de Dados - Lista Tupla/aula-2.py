# Operador IN

a = 10
b = 25
c = 66

# x = int(input("Digite um numero: "))
#
# #if(x ==a or x==b or x==c):
#
# if(x in [a,b,c]):
#     print("Esta contido")
# else:
#     print("Não esta contido")

#---------------------------------------------


cores = [" azul, amarelo, vemelho, branco "]

while True:
    cor = input("Digite o nome de uma cor ou então,\n "
                  "0 para sair do programa: ")
    if(cor=="0"):
        break
    elif cor in cores:
        print("Essa cor esta contida!")
    else:
        print("Essa cor não esta contida!")




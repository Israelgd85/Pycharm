# 9) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
# solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação.
#  Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:

print()
print("Estou em loop")
print()
l = input("Digite a letra Q para sair do loop: ")

while (l != "q" or l!="Q"):

    if (l=="q" or l=="Q"):
        print("Loop terminado")
        break

    elif (l!="q" or l!="Q"):
        print("Estou em loop")
        l = input("Digite a letra Q para sair do loop: ")
        continue



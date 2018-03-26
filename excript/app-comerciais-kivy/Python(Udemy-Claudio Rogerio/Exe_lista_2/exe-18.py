#18)Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano.
#Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida.
#Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.


data = input("Informe a data desejada no formato dd/mm/yyyy: ")
cont = len(data)


if cont < 10:
    print("O formato esta errado, digite no seguinte formato dd/mm/yyyy")
    print()
    data = input("Informe a data desejada no formato dd/mm/yyyy: ")
print()
print(data)


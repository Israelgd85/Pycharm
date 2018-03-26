#17) Faça um algoritmo que receba um número inteiro, que represente um
# determinado mês do ano, e mostre o nome do mês correspondente.
# Por exemplo, se for informado o número 2, o algoritmo deverá exibir: fevereiro.
# O algoritmo também deve validar se a entrada está correta.

mes = int(input("Informe o numero que representa o mês do ano: "))



if mes == 1:
    print("Janeiro")

if mes == 2:
    print("Fevereiro")
if mes == 3:
    print("Março")
if mes == 4:
    print("Abril")
if mes == 5:
    print("Maio")
if mes == 6:
    print("Junho")
if mes == 7:
    print("Julho")
if mes == 8:
    print("Agosto")
if mes == 9:
    print("Setembro")
if mes == 10:
    print("Outubro")
if mes == 11:
    print("Novembro")
if mes == 12:
    print("Dezembro")
if mes < 0 or mes > 12:
    print("Mês inválido!!!")


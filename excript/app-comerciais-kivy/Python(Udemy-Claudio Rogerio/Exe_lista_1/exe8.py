#Básico I 8) Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário.
# Em seguida, calcule e envie para a saída padrão a média:

print()
print("Calcule a sua média")
print()

nota1 =  float(input("Informe a sua primeira nota: "))
nota2 =  float(input("Informe a sua segunda  nota: "))
nota3 =  float(input("Informe a sua terceira nota: "))
nota4 =  float(input("Informe a sua quarta   nota: "))

media = ((nota1+nota2+nota3+nota4)/4)
print()

print("Sua média é: ",media)


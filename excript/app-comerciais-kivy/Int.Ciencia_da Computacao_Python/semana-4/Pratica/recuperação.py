alunos = int(input("Informe o numeros de alunos: "))
recuperacao = 0
n = 0
media = 0
while alunos > n:
    print()
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))
    media = (nota1+nota2+nota3+nota4)/4
    n += 1
    print("Média: ", media)
    print()
    if media <= 5.0 or media <= 3.0:
        recuperacao += 1
        if media < 3.0:
            recuperacao -= 1
            print("Reprovado !")

print()
print("Alunos em recuperação: ", recuperacao)
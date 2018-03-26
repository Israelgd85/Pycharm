#Variaveis Booleanas

decrescente = True

anterior = int(input("Digite o primeiro numero da sequência: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite próximo numero da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("A sequência esta em ordem decrescente!")
else:
    print("Asequencia não está em ordem descrescente!")
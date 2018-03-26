tamanho = int(input("Digite o tamanho da sequencia de numeros: "))
i=0
print("Digite uma sequência de valores terminadas por zero.")
produto = 1
valor = 1

while i < tamanho :
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i += 1
print("O produto dos valores digitados é: ", produto)
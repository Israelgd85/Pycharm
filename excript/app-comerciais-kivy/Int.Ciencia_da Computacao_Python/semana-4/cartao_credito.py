meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNalista = False

while cartaoLido != 0 and not encontreiMeuCartaoNalista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNalista = True

if encontreiMeuCartaoNalista:
    print("Meu cartão está na lista")
else:
    print("Meu cartão não está na lista")
#Basico I 14) Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida,
#aplique 10% de desconto e imprima na tela tanto o valor total como também o valor com o desconto aplicado.


compra = float(input("Informe o valor da compra: "))
desc = compra-(compra*0.10)

print("Valor da compra",compra)

print("Total a pagar de desconto: %.2f"%desc)


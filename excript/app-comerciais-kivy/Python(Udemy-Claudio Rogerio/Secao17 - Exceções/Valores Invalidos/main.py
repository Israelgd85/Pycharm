def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número Inválido")

num1 = input_float("Digite o primeiro numero: ")
num2 = input_float("Digite o segundo numero: ")


try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Não é possível dividir um número po zaro")



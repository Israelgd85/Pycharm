#20) Escreva uma função que verifica se uma String enviada é um palíndromo ou não.

palavra = input("Informe uma palavra: ")
def func_palindromo(palavra):
    if palavra == palavra[::-1]:
        print("A palavra" ,palavra, "é um palindromo")
    else:
        print("A palavra" ,palavra, "não é um palindromo")

func_palindromo(palavra)
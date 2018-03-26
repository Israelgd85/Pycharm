# 8) Escreva um algoritmo capaz de receber uma quantidade variável
# de parâmetros que estejam associados a uma chave. Em seguida,
#  imprima na tela o nome da chave e o respectivo valor:


def fun (**kwargs):
    print(kwargs)

fun( NOME="Israel", idade = 32, Nacionalidade="Brasileiro")
# 21) Escreva uma função que tenha definida uma função em seu escopo.
#  Invoque a função aninhada, retorne algum valor, imprima esse valor
#  na tela e finalize a aplicação.


def func1():


    def func2(*args):
        print(args)
        return args

    func2(1,2,3,4,5)

func1()
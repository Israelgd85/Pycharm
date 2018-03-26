#Desempacotamento


# lista = [10, 20]
#
# def func (a, b):
#     print()
#
# func(*lista)
# # func(10, 20)
# # func(a=10, b=20)



def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

#tupla = "eXcript","Brasil",20
#lista = ["eXcript","Brasil",20]

#pessoa(tupla[0],tupla[1],tupla[2])
#pessoa(*lista)

d = {"nome":"eXcript", "sobrenome":"Brasil", "idade":20} #Dicionario
pessoa(**d)

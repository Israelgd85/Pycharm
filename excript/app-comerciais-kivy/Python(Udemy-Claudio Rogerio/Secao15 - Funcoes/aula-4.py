#Argumentos Posicionais e Argumentos nomeados

def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))

#dados_pessoais("Claudio", "Rogerio", 30, True)
#dados_pessoais(nome="Claudio", sobrenome="Rogerio", idade=30, sexo=True)
# dados_pessoais(idade=30,
#                sexo=True,
#                nome="Claudio",
#                sobrenome="Rogerio",
#                )
dados_pessoais("Claudio", sobrenome="Rogerio", idade=30, sexo=True)

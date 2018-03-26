#coding: utf-8
#JOGO do NIM

def main ():
    iniciar = partida()
    op = input("Escolha opcção 1 ja jogada unica ou 2 para campeonato: ")
    i = 0
    if op == 1:
        iniciar
    elif op == 2:
        while i <3:
            iniciar
        i += 1



def computador_escolhe_jogada (n,m):
    if (m-n) % (m+1) == 0:
        n = (n - (m+1))
        print("O computador tirou", m, "peças")
        print("Agora restam", n,"no tabuleiro")
        return n
    else:
        n = n - m
        print("O computador tirou", m, "peças")
        print("Agora restam", n, "no tabuleiro")
        return n

def usuario_escolhe_jogada (n,m):
    pecas = int(input("Quantas pecas você vai tirar? "))

    if pecas > m:
        print("Oops! Jogada inválida! tente de novo")
        pecas = int(input("Quantas pecas você vai tirar? "))

    if m >= pecas:
        n = n - pecas
        print("Você tirou", pecas, "peças")
        print("Agora resta apenas", n, "peças no tabuleiro")
        return n

def partida ():
    n = int(input("Quantas peças: "))
    m = int(input("Limite de peças por jogada: "))

    if n % (m+1) == 0:

        print("Computador começa")
        computador_escolhe_jogada(n,m)
    else:
        print("Usário comceça")
        usuario_escolhe_jogada(n,m)









# def campeonato () :
#     op1 = int(input("1 - para jogar uma partida isolada"))
#     op2 = int(input("2 - para jogar um campeonato"))

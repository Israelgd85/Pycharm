# def desenha(linha):
#     while linha > 0:
#         coluna = 1
#         while coluna <= linha:
#             print('*', end = "")
#             coluna = coluna + 1
#         print()
#         linha = linha - 1
#
# desenha(5)




altura = 5
linha = 1
while linha <= altura:
    print("*", end ="")
    coluna = 2
    while coluna < altura:
        if linha == 1 or linha == altura:
            print("*", end ="")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1

# x = 1
# while x < 3:
#     y = 1
#     while y < 3:
#         print(x*y, end = "\t")
#         y = y + 1
#     x = x + 1
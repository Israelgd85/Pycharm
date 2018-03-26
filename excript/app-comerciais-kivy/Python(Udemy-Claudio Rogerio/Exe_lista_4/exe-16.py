# 16) Escreva uma função que aceite Strings e calcule a quantidade de letras
# em mauisculas e minúsculas que a String possui.

s = 'IteRando StriNgs'

def func_maiusc (n):
    indice = 0
    maiusc = 0
    mini = 0
    while indice < len(s):
        cut = s[indice]
        asc = ord(cut)
        indice+=1
        if asc <= 90 and asc >=65:
            maiusc +=1
        else:
            mini += 1
    print("Aquantidade de letras Maiusculas é: ", maiusc)
    print("A quantidade de letras Minusculas é: ", mini)
func_maiusc(s)




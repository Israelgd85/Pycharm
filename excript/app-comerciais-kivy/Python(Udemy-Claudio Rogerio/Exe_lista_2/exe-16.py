#16) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E.
# Os endereços no intervalo de 0 à 127 são classe A, de 128 a 191 são classe B,
# de 192 a 223 são classe C,# de 224 à 239 são classe D e a partir de 240 são classe E.
# Faça um algoritmo que leia o primeiro octeto,
# no formato decimal de um endereço IP, e informe a sua classe.

ip  = int(input("Informe o primeiro Octeto do enderço IP: "))


if ip >= 0 and ip <= 127 :
    print("IP Clasee A")
elif ip >= 128 and ip <= 191 :
    print("IP Classe B")
elif ip >=192 and ip <= 223 :
    print("IP Classe C")
elif ip >= 224 and ip <= 239 :
    print("IP Classe D")
else:
    print("IP Classe E")




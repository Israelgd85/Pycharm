import math

xa = int(input("Digite a primeira distância do ponto A:"))
ya = int(input("Digite a segunda distância do ponto A:"))
xb = int(input("Digite a primeira distância do ponto B:"))
yb = int(input("Digite a segunda distância do ponto B:"))

d = math.sqrt(((xb-xa)**2)+((yb-ya)**2))

if(d >= 10):
    print("longe")
else:
    print("perto")
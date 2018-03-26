#Basico I 13) Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas,
# minutos e segundos. Em seguida, converta tudo para segundos:

day  = 86400
hour = 3600
min  = 60

dia  = int(input("Digite o numeros de dias: "))
hora = int(input("Digite a quantidade de horas: "))
mini = int(input("Digite a quantidade de minutos: "))
seg  = int(input("digite a quantidade de segundos: "))

print()

vd = dia*day
vh = hora*hour
vm = mini*min

total = vd+vh+vm+seg

print("Total de dias em seg = ", vd)
print("Total de horas em seg = ", vh)
print("Total de minutos em seg =", vm)
print()

print("A soma do total em seg: ",total)



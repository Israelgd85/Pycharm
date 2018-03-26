# Iterando lista em Python

#lista_nums = [100,200,300,400]
#O codigo abaixo não funciona
#for item in lista_nums:
#    item += 1000
#print(lista_nums)

#lista_nums = [100,200,300,400,500,600,700,800]
    #{lista_indice = [0,1,2,3]
    #lista_indice = range(4)
    #for item in range(4):}
#for item in range(len(lista_nums)):
#    lista_nums[item] += 1000
#print(lista_nums)


#Função de nome enumerate
lista_nums = [100,200,300,400,500,600,700,800]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)
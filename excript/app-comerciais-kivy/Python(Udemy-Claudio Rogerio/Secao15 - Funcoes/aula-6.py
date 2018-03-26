#Retorno de Valores multiplos

# def func():
#     return 1, 2
#
# a, b = func()
#
# #a ,b = 10, 20
# #t = (10, 20, 3)
# #a, b, c = t
#
# print(a)
# print(b)

def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo

q,c = potencia(10)


print(q)
print(c)

# 6) Faça um algoritmo que imprima os números primos entre 0 e 100:



for i in range(2, 100):
    n = 0
    p = 0
    div = 0
    while p < 100:
        p += 1
        n += 1
        if (i % n == 0):
            div+=1
            continue
    if (div==2):
       print(i)






















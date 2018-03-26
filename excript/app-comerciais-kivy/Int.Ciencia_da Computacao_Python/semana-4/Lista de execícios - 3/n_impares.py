n = int(input("digite o valor d n: "))
i=0
imp = 0
while i < n:
    if imp%2==0:
       imp += 1
    elif imp%2!=0:
        print(imp)
        i += 1
        imp += 1



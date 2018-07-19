class Bichos:
    qnt_bichos = 0
    def __init__(self):
        self.add_bicho()
    def __del__(self):
        self.del_bichos()
        if (self.qnt_bichos==0):
            print("Todos os bichos foram mortos!")
    def add_bicho(cls):
        cls.qnt_bichos += 1
    def del_bichos(cls):
        cls.qnt_bichos -= 1

    add_bicho = classmethod(add_bicho)
    del_bichos = classmethod(del_bichos)




b1 = Bichos()
print(Bichos.qnt_bichos)
b2 = Bichos()
print(Bichos.qnt_bichos)
b3 = Bichos()
print(Bichos.qnt_bichos)

del(b1)
print(Bichos.qnt_bichos)
del(b2)
print(Bichos.qnt_bichos)
del(b3)
print(Bichos.qnt_bichos)


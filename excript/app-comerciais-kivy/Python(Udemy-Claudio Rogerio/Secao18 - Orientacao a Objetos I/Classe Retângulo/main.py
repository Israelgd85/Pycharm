#coding: utf-8

__author__= "Israel Gomes Deconto"

class Retagulo:

    def __init__(self):
        self.a = 0
        self.l = 0

    def area(self):
        return self.a * self.l

r1 = Retagulo()
r1.l = 10
r1.a = 5

r2 = Retagulo()
r2.l = 20
r2.a = 20

print(r2.area())
print(r1.area())



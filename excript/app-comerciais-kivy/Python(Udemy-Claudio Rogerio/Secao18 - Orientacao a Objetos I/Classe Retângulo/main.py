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

print(r1.area())



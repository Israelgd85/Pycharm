#coding: utf-8

__author__= "Israel Gomes Deconto"


class A:
    def __init__(self):
        print(id(self))
a = A()
print(id(a))
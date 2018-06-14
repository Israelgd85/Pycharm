#coding: utf-8

__author__= "Israel Gomes Deconto"

class AAA:
    pass

bbb =AAA()

AAA.var_cls = "AAA.var_cls"
bbb.var_cls = "bbb.var_inst"

bbb.var_cls = "bbb.var_cls"


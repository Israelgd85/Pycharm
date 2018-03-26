# 9) Considere o trecho de código a seguir.

#Invoque a função func(), passando como argumento os valores contidos em lista,
#  com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:



def lista (*lista):
    return lista

a,b,c,d,e,f = lista(1,2,3,4,5,6,)

print("",a,"\n",
      b,"\n",
      c,"\n",
      d,"\n",
      e,"\n",
      f)



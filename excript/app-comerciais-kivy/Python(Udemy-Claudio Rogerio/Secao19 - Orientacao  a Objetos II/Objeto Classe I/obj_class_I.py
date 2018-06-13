Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> class MinhaClasse:
	pass

>>> obj = MinhaClasse()
>>> type(obj)
<class '__main__.MinhaClasse'>
>>> type(MinhaClasse)
<class 'type'>
>>> obj.__class__
<class '__main__.MinhaClasse'>
>>> MinhaClasse.__class__
<class 'type'>
>>> obj.__name__
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    obj.__name__
AttributeError: 'MinhaClasse' object has no attribute '__name__'
>>> MinhaClasse.__name__
'MinhaClasse'
>>> obj.__class__.__name__
'MinhaClasse'
>>> 
>>> 
>>> 
>>> MinhaClasse.var_cls = 0
>>> print(MinhaClasse)
<class '__main__.MinhaClasse'>
>>> MinhaClasse.__dict__
mappingproxy({'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MinhaClasse' objects>, '__weakref__': <attribute '__weakref__' of 'MinhaClasse' objects>, '__doc__': None, 'var_cls': 0})
>>> from pprint import pprint
>>> pprint(MinhaClasse.__dict__)
mappingproxy({'__dict__': <attribute '__dict__' of 'MinhaClasse' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'MinhaClasse' objects>,
              'var_cls': 0})
>>> pprint(obj.__dict__)
{}
>>> obj.var_cls
0
>>> 

>>> MinhaClasse.var_cls = 10
>>> obj.var_cls
10
>>> 

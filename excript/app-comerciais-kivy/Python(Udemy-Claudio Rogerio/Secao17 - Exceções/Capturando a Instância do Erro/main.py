def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e))
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError):
        print("NameErros ocorreu ou então, NameError")




#TypeError
erro("int+int")

#NameError
erro("a")

#ValueError
erro("int('a')")

#ZeroDivisionError
erro("5/0")
erro("10+10")

print("A aplicação foi finalizada")
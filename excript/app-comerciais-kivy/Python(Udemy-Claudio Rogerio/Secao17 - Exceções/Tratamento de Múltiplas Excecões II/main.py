def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
            print("NameError ocorreu ou então, NameError")
    except ValueError:
            print("ValueError")
    except ZeroDivisionError:
            print("ZeroDivisionError")



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
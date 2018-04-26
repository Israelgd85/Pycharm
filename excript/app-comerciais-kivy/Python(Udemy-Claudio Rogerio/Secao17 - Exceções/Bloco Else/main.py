def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e)) #instância da exceção

    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError)as e:
        print("NameErros ocorreu ou então, NameError")
        print(type(e))  # instância da exceção
    else:
        print("Nenhuma exceção ocorreu.")
    finally:
        print("sempre sera executado.")


#TypeError
erro("int+int")

#NameError
erro("a")

#ValueError
erro("int('a')")

#ZeroDivisionError
erro("5/0")
erro("10+10")

print("A aplica ção foi finalizada")
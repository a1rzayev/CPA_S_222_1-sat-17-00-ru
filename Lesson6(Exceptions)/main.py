try: # код, который может вывести ошибку
    a = int(input("a: "))
    b = int(input("b: "))
    print("a / b =", a / b) # ValueError or ZeroDevisionError

except ZeroDivisionError: # что делать при ошибке(отладчики)
    print("на 0 делить нельзя!")

except ValueError:
    print("неверные числа!")

except Exception as e:
    print("неизвестная ошибка!", e)

else: # если не сработали отладчики исключения
    print("все окей!")

finally: # всегда выполняется(файналайзер)
    print("финально все окей!")
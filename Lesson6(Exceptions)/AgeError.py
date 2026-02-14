import warnings

class AgeError(Exception):
    pass

print("добро пожаловать в автошколу. здесь вы получите права!")
age = int(input("введите возраст: "))

if (age < 18 and age >= 16):
    warnings.warn("вам можно получить права на мопеды", UserWarning)
if (age < 16):
    raise AgeError("вам нет достаточно лет для получения прав") 


print("доступ разрешён")
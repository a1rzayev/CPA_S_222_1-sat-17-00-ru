"""Декораторы"""



def checker(function): # передаем функцию в декoратор, чтобы охватывать его
    def wrapper(*args, **kwargs): # передаем аргументы функции в наш декоратор
    # проверяем через try & правильно работает или нет
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"Error in: {exc}")
        else:
            print(f"No Problems. Result: {result}")
            return result
    return wrapper # возвращаем декоратор

@checker # указываем декоратор на нашу функцию
def calculate(expression):
    return eval(expression)

# всё окей
calculate("2 + 2")
# ошибка
calculate("2 / 0")
import unittest # модуль юнит-тестов(проверки функций и классов. каждого юнита(элемента))

# создаём функции
def add(a, b): # добавить
    return a + b

def subtract(a, b): # вычитать
    return a - b

def multiply(a, b): # умножить
    return a * b

def divide(a, b): # поделить
    if(b == 0): 
        raise ZeroDivisionError("ай бала нельзя делить на 0! уже третий урок я тебе это пытаюсь объяснить!")
    else:
        return a / b    

divide(10, 5)
# divide(10, 0)

# создаем юнит-тест класс
class TestCalculator(unittest.TestCase):
    # проверка функции добавления
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    # проверка функции вычитания
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, 3), 4) # неправильное выполнение
        self.assertEqual(subtract(0, 4), -4)
    # проверка функции деления
    def test_multiply(self):
        self.assertEqual(multiply(10, 2), 20)
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(4, 2), 8)
    # проверка функции деления
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(3, 2), 1.5)
        self.assertEqual(divide(4, 2), 2)
        # создаем область определения с возможностью ошибки деления на ноль и проверяем
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()



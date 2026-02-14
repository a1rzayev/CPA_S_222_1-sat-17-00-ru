import inspect
import math

# интроспекция функции
def add(a:int, b:int) -> int:
    return a + b

print(inspect.getdoc(add)) # даёт документацию к функции
print(inspect.signature(add)) # требуемые аргументы и возвращаемое значения
print(inspect.getsource(add)) # весь код функции



# интроспекция класса
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        return f"{self.name}: {self.grade}" 
    
print(inspect.getdoc(Student)) # даёт документацию к функции
print(inspect.signature(Student)) # требуемые аргументы и возвращаемое значения
print(inspect.getsource(Student)) # весь код функции



# интроспекция модуля
members = inspect.getmembers(math)

for name, obj in members:
    if inspect.isfunction(obj):
        print(name)

print(inspect.getdoc(math.sqrt)) # даёт документацию к функции
print(inspect.signature(math.sqrt)) # требуемые аргументы и возвращаемое значения
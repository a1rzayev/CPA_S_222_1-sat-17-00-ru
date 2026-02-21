"""Итерация(пересчитывание) списка"""



my_list = [1, 2, 3, 4, 5]
# указываем итератор(счётчик) на наш список
iterator = iter(my_list)

print(next(iterator)) # следующий элемент в перечисление
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# будет ошибка StopIteration из-за окончания элементов в списке
# print(next(iterator))

# указание next() через for
for elem in iterator:
    print(elem)

# пример с классом
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        self.i += 1
        if (self.i > self.max_number):
            return StopIteration # возвращает одно значение
        return self.i
    
counter = Counter(10)
counter.__iter__()
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())

for elem in counter:
    print(elem)
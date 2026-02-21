"""Генераторы"""



# с циклом for
def raise_to_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i # возвращает несколько значений одновременно
        i += 1

result = raise_to_degrees(5, 5)
print(result)
for _ in result:
    print(_)



# с циклом while 
def raise_to_degrees(number, max_degree):
    i = 0
    while(i < max_degree):
        yield number ** i # возвращает несколько значений одновременно
        i += 1

result = raise_to_degrees(5, 5)
print(result)
for _ in result:
    print(_)
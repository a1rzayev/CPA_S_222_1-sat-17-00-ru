# библиотека с информацией о системе и модулях
import sys 

print(sys.version) # версия системы
print(sys.platform) # платформа системы

# все загруженные модули
print("All modules:")
for module_name in list(sys.modules.keys()):
    print(module_name)

# где python ищет модули
print("All paths:")
for path in sys.path:
    print(path)


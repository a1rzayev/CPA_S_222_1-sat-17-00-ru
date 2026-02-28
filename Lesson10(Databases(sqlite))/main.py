import sqlite3



"""простое подключение"""
# создаем подключение к базе данных
connection = sqlite3.connect("db.sl3")

# подключаем курсор
cur = connection.cursor()

print(connection)
print(cur)
# обязательно закрываем поток
connection.close()



"""создание таблицы"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

# выполняем скрипт позволяющий создать новую таблицу
cur.execute("CREATE TABLE students (name TEXT);")

# подтверждаем наши изменения
connection.commit()
connection.close()



"""добавление элементов в таблицу"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

# выполняем скрипт позволяющий добавить элемент в таблицу
cur.execute("INSERT INTO students (name) VALUES ('Farhad')")
cur.execute("INSERT INTO students (name) VALUES ('OptimusPrime')")
cur.execute("INSERT INTO students (name) VALUES ('BulBulBuulBuldog')")
cur.execute("INSERT INTO students (name) VALUES ('Rasul bratik')")

# подтверждаем наши изменения
connection.commit()
connection.close()



"""вывод элементов из таблицы"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

# выполняем скрипт позволяющий взять элемент(-ы) из таблицы
cur.execute("SELECT name FROM students")

# подтверждаем наши изменения
connection.commit()
res = cur.fetchall()
print(res)
connection.close()



"""удаление элемента"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

# выполняем скрипт позволяющий удалить элемент из таблицы
cur.execute("DELETE FROM students WHERE(name == 'OptimusPrime')")

# подтверждаем наши изменения
connection.commit()
connection.close()



"""обновление элемента"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

# выполняем скрипт позволяющий изменить элемент из таблицы
cur.execute("UPDATE students SET name='Murad Otlichnik' WHERE(name == 'BulBulBuulBuldog')")

# подтверждаем наши изменения
connection.commit()
connection.close()



"""удаление таблицы"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

# выполняем скрипт позволяющий удалить таблицу
cur.execute("DROP TABLE students")

# подтверждаем наши изменения
connection.commit()
connection.close()
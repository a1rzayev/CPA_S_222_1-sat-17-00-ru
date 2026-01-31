# неправильно! при удалении одного из элементов, все испортятся!
name_list = ["Rafael", "Farxad", "Jahangir", "Rasul"]
surname_list = ["Zabirov", "Sadig", "Asadbayli", "Huseynov"]
age_list = [12, 15, 14, 13]
# print(name_list[1])
# print(surname_list[1])
# print(age_list[1])

# класс(тип данных, который создали мы сами) человека
class Person:
    def __init__(self, birthyear1, name1, surname1, pol1):
        self.birthyear = birthyear1
        self.name = name1
        self.surname = surname1
        self.pol = pol1
        self.hobbies = []

farxad = Person(2011, "Farxad", "Sadig", "M")
aysu = Person(2012, "Aysu", "Aliyeva", "F")

# print(aysu.birthyear)
# print(aysu.name)
# print(aysu.surname)
# print(aysu.pol)


class Student:
    def __init__(self, name1, surname1, birthyear1, avg_grade1, course1 = "MKA"):
        self.name = name1
        self.surname = surname1
        self.birthyear = birthyear1
        self.course = course1
        self.hobbies = []
        self.avg_grade = avg_grade1

    def study(self):
        print(f"{self.name} is studying")

    def show_info(self):
        print(f"{self.name} {self.surname} : {self.course}")
        print(f"avg_grade: {self.avg_grade}")
        print(f"age: {2026 - self.birthyear}")
        print(f"hobbies: {self.hobbies}")

Emil = Student("Emil", "Aslanov", 2012, 9.3, "PKO")
Emil.show_info()
Emil.study()
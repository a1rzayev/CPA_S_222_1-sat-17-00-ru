import random



# класс(пользовательский тип данных) работы
class Job:
    # конструктор(назначает значения при создании)
    def __init__(self, name:str = "test_job", salary:float = 1):
        self.name = name
        self.salary = salary

    """сеттеры(изменяют значения параметров)"""
    # сеттер для имени
    def set_name(self, name:str):
        self.name = name

    # сеттер для зарплаты
    def set_salary(self, salary:float):
        self.salary = salary



# класс(пользовательский тип данных) человека
class Human:
    # конструктор(назначает значения при создании)
    def __init__(self, name:str = "name", job:Job = None,
                 home = None, car = None, money:float = 0):
        self.name = name
        self.job = job
        self.home = home
        self.happiness = 100
        self.satiety = 100
        self.car = car
        self.money = money

    """сеттеры(изменяют значения параметров)"""
    # сеттер для имени
    def set_name(self, name:str):
        self.name = name

    # сеттер для дома
    def set_home(self, home):
        self.home = home

    # сеттер для машины
    def set_car(self, car):
        self.car = car

    # сеттер для работы
    def set_job(self, job:Job):
        self.job = job

    """функции"""
    # функция покушать
    def eat(self):
        self.satiety += 10

    # функция получать зарплату
    def work(self):
        self.money += self.job.salary



# работы
programmist = Job("programmist", 3000)
futbolist = Job("futbolist", 2000)
dizayner = Job("dizayner", 2500)

# люди
Farkhad = Human("Farkhad", programmist, "mardakan_dacha", "MB_Maybach", 250)
Vidadi = Human("Vidadi", futbolist, "badamdar_dacha", "07_peredok", 150)
Aysu = Human("Aysu", dizayner, "28may", "Porsche", 250)

# список людей
people_list = [Farkhad, Vidadi, Aysu]

Farkhad.eat() # ест
Farkhad.work() # зарабатывает

programmist.set_salary(4000)
programmist.set_name("developer")

for person in people_list:
    print(f"Job:\n\tName: {person.job.name} \n\tSalary: {person.job.salary}")
    print(f"Human:\n\tName {person.name} \n\tJob: {person.job.name}({person.job.salary}) \n\tHome: {person.home} \n\tCar: {person.car} \n\tHappiness: {person.happiness} \n\tSatiety: {person.satiety} \n\tMoney: {person.money}")


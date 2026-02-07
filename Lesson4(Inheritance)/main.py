# класс(пользовательский тип данных) двигателя
class Engine:
    def __init__(self, volume:float, horse_power:float, torque:float):
        self.volume = volume
        self.horse_power = horse_power
        self.torque = torque

    def start(self):
        print("engine started")

    def stop(self):
        print("engine stopped")



# класс(пользовательский тип данных) коробки передач
class Transmission:
    def __init__(self, type:str = "automatic"):
        self.type = type



# класс(пользовательский тип данных) транспорта с возможностью водить
class Drivable:
    def __init__(self, wheels_count:int, seats_count:int):
        self.wheels_count = wheels_count
        self.seats_count = seats_count

    def drive(self):
        print("driving...")


# класс(пользовательский тип данных) машины -> drivable
class Car(Drivable):
    def __init__(self, transmission:Transmission, engine:Engine, seats_count:int = 5):
        self.transmission = transmission
        self.engine = engine
        self.wheels_count = 4
        self.seats_count = seats_count



# класс(пользовательский тип данных) велосипед -> drivable
class Bicycle(Drivable):
    def __init__(self, seats_count:int = 1):
        self.wheels_count = 2
        self.seats_count = seats_count


# моторы машин
m113 = Engine(5.0, 306, 400)
n52 = Engine(3.0, 268, 300)

# коробки машин
automatic_transmission = Transmission()
manual_transmission = Transmission("manual")

vehichle = Drivable(0, 0)
mercedes_w211 = Car(automatic_transmission, m113)

print(f"Car: \n\tWheels: {mercedes_w211.wheels_count} \n\tSeats: {mercedes_w211.seats_count} \n\tTransmission: {mercedes_w211.transmission.type}")
print(f"Engine:\n\tVolume: {mercedes_w211.engine.volume}L \n\tPower: {mercedes_w211.engine.horse_power}HP \n\tTorque: {mercedes_w211.engine.torque}Nm")

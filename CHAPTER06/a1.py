class Car:
    weight = 4000
    num_wheels = 4

    def __init__(self, car_name="NoName"):
        self.name = car_name

    def calc_wehith_per_wheel(self):
        return self.weight / self.num_wheels


default_car = Car()


my_car = Car()
print(my_car.calc_wehith_per_wheel())
print(default_car.name)
my_car = Car("Delorean")
print(my_car.name)

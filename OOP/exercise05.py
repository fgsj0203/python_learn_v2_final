"""
Creating class "Car" with counter instances
"""


class Car:
    counter_car = 0

    def __init__(self, model):
        self.model = model
        Car.counter_car += 1


c1 = Car("Volkswagen")
c2 = Car("Chevrolet")

print(f"The amount car is {Car.counter_car} cars ")

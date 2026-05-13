from abc import \
    ABC, \
    abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        ...
    @abstractmethod
    def refuel(self):
        ...


class Car(Vehicle):
    CONDITIONER_ON = 0.9


    def drive(self, distance):
        consumption = (self.CONDITIONER_ON + self.fuel_consumption) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):

    CONDITIONER_ON = 1.6
    def drive(self, distance):
        consumption = (self.CONDITIONER_ON + self.fuel_consumption) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95




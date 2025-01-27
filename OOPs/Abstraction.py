'''
Abstraction:
    Abstracion is the concept of hiding the complex implementation details and showing only the necessary features of an 
    object. This helps reducing complexity and effort.
'''

from abc import ABC,abstractmethod

## Abstract Base Class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is sued for driving")
    
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("The car is started")

def operate_vehicle(Vehicle):
    Vehicle.start()

car = Car()
operate_vehicle(car)  # Output: The car is started.

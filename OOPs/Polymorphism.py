"""
Polymorphism is a core concept in OOPs that allows objects of different classes to be treated as objects of
a common superclass. It provides a way to perform a way to perform a single action in differnt forms.
poltmorphism is typically acieved through method overriding and interfaces.
"""

"""
Method Overriding - Method Overriding allows a child class to provide a specific implementation of a 
method that already defined in its parent class.
"""
## Base Class

class Animal:
    def speak(self):
        return "Sound of the animal"

## Derived Class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
## Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

## Function that demonstrates Polymorphism
def make_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

make_sound(dog)

### Polymorphsim with functions and methods
## Base Class
class Shape:
    def area(self):
        return "The area of the figure"
    
## Derived Class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

## Derived Class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius

## Function that demostrates polymorphism

def print_area(shape):
    print(f"The area is {shape.area()}")

cirle = Circle(5)
rectangle = Rectangle(4, 5)
print_area(cirle)
print_area(rectangle)

"""
Polymorphism with Abstract Base Classes:
Abstract Base Classes are used to define common methods for a group of related objects. They can
enforce that derives classes implement particular methods, promoting consistency across different
implementations.
"""
from abc import ABC, abstractmethod

## Define an abstract base class

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Derived Class 1
class Car(Vehicle):
    def start_engine(self):
        return "The car engine is started"
    
# Derived Class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "The motorcycle engine is started"
    
# Function that demonstrates polymorphism with abstract base classes
def start_vehicle(vehicle):
    print(vehicle.start_engine())

## create objects of car and motorcyle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)
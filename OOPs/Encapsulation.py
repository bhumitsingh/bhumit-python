"""
Encapsulation is the concept of erapping data(variables) and methods(functions) together as a single
unit. It restricts direct access to some of the objects components, which is a means of preventing
accidental interference and misuse of the data.
"""

### Encapsulation with getter and setter methods
## Public, protected, private variables or access modifiers.

#Public Varible
class Person:
    def __init__(self, name, age):
        self.name = name ## public variable
        self.age = age ## public variable
    
def get_name(person):
    return person.name
    
person = Person("John", 30)
print(get_name(person))

## Private Variable
class Person2:
    def __init__(self, name, age,gender):
        self.__name = name ## private variable
        self.__age = age ## private variable
        self.gender = gender
    
person2 = Person2("John", 30, "Male")
print(dir(person2))

## Protected variable
class Person2:
    def __init__(self, name, age,gender):
        self._name = name ## protected variable
        self._age = age ## protected variable
        self.gender = gender

class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    
    
employee = Employee("John", 30, "Male")
print(employee._name)

'''
Object Oriented Programming is a programming paradigm that uses "ibjects" to design applications and
computer programs. OOP allows for modelling real-world scenarios using classes and objects.
'''
## A class  is a blueprint for creating objects. Attributes, methods

class Car:
    pass

audi=Car()
bmw=Car()

print(type(audi))


print(audi)
print(bmw)

audi.windows = 4 #Initializing attiributes like this is not the proper way
bmw.windows = 4
print(audi.windows)
print(bmw.windows) 

tata = Car()
tata.windows = 4
print(tata.windows)


#Instance Variables and Methods
class Dog:
    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
## Create object
dog1 = Dog("Bella", 3)
dog2 = Dog("Max", 5)
print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog2.age)

class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited into your account. New balance is {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:    
            self.balance -= amount
            print(f"{amount} is withdrawn from your account. New balance is {self.balance}")
    def getBalance(self):
        return self.balance

account = BankAccount("Bhumit",5000)
print(account.balance)

account.deposit(5000)
account.withdraw(1000)
account.withdraw(100000)
print(account.getBalance())
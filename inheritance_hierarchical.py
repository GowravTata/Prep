"""
Inheritance in which multiple classes inherit from a single parent class
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow!")


fido = Dog("Storm")
fido.bark()

felix = Cat("Potter")
felix.meow()

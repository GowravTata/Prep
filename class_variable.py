# Class variables are declared inside a class definition
# Changing the class variable by an object is bound to that object
"""
For a class variable it is recommended to call using the Class instead of an object,
if we try to change it using the object, it creates a new instance variable that shadows over the class variable
for that object
"""


class Car:
    country = 'Germany'

    def __init__(self, make, name, country):
        self.make = make
        self.name = name
        self.country = country
        # A class variable can also be accessed from inside the constructor
        # print(self.country)

    def display(self):
        return self.country

    @classmethod
    def class_display(cls, make, name, country):
        return cls(make, name, country)

    @classmethod
    def change_country(cls, name):
        cls.country = name

    @classmethod
    def class_country(cls):
        return cls.country


polo = Car('VW', 'polo', 'UK')
print('Before changing the country')
print(Car.country)  # Germany

print(polo.country)  # UK , because the instance variable overshadows the class variable
polo.country = 'Italy'  # Changing the country by an object will not make the changes to the class
polo.change_country('Sweden')
print('After changing the country')
print(polo.display())  # Italy , because the method refers to the instance variable
print('After changing the country fetching the class variable')
print(polo.class_country())

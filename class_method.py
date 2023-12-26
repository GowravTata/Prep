# Class variables can be accessed from both instance and class method
from datetime import date


class FoodChain:
    country = 'USA'

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @classmethod
    def change_country(cls, country):
        """
        Only a class method can change the class variable
        class method cannot access the instance variables, can access only class variables
        """
        cls.country = country
        return cls.country

    def origin(self):
        return self.country

    @classmethod
    def change_constructor(cls, brand, year):
        return cls(brand, year)

    def getattr(self):
        return f'Franchise {self.brand} established in {self.year}'


kfc = FoodChain('kfc', 1968)
print('Before changing origin country :', kfc.origin())

kfc.change_country('Germany')
print('After changing origin country :', kfc.origin())

# Checking the country variable of class , directly from class, to confirm whether the changes are made from
print(FoodChain.country)

mcd = FoodChain('McDonald', 1923)
print(mcd.getattr())
print(getattr(mcd, "year"))  # 1923 , this fetches the attribute present in the class

# Changing the constructor of the class by using change_constructor method
mcd = mcd.change_constructor('BurgerKing', 1856)
print(mcd.getattr())


# Dynamically adding the class method to the class
def get_country(cls):
    print(cls.country)


FoodChain.get_country = classmethod(get_country)

starbucks = FoodChain('Star Bucks', 1990)
print('Checking if the class has a certain method')
print(hasattr(starbucks, 'get_country'))
starbucks.get_country()

# Dynamically deleting the class method from a class
del FoodChain.get_country

# Checking if the method exists in the class
print(hasattr(starbucks, 'get_country'))

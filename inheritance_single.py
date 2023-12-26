"""
It is the way of using the class that is already defined
"""

"""
Single Inheritance is a property from OOPS, which allows new classes to acquire the properties and methods of 
existing class
"""


class Bottle:
    name = ""

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drink(self):
        print("You can drink")
        return

    def __repr__(self):
        return repr(f"{self.brand} brand in {self.year}")


class Sprite(Bottle):
    def __init__(self, brand, year, name, expire):
        super().__init__(brand, year)
        self.name = name
        self.expire = expire

    def drink(self):
        super().drink()  # This can be used to call the method in the super class
        return "You can drink sprite"

    def __repr__(self):
        return repr(f"Defined attributes are {self.brand} brand in {self.year} and {self.name} which expires"
                    f"on {self.expire}")


bottle = Sprite('Coke', 2023, 'Cola', 2024)

print(bottle.drink())

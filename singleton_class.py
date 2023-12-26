"""
Single ton method is one which allows to provide one and only object of a particular type
"""

"""
Below two instances are created when it is printed it displays only the attributes of the last object that is created
The instances created from the class have the same reference
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class DerivedSingleTon(Singleton):
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = DerivedSingleTon('First', 1)
obj2 = DerivedSingleTon('Second', 2)
print(obj1.name, obj2.name)
print(obj1.age, obj2.age)

print(obj1 == obj2)

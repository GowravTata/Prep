from dataclasses import dataclass, field
import random
import string

from typing import List

"""
Data Classes help mainly in data oriented classes
"""


@dataclass(order=True)
class Investor:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    cash: int = field(repr=True, default=0)

    def __post_init__(self):
        self.sort_index = self.cash


# i1 = Investor('Bobby', 27, 700)
# i2 = Investor('Tata', 64, 7000)
# i3 = Investor('Bobby', 27)
#
# print(i1 < i2)


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=12))


@dataclass(frozen=False)  # If kept as true, then the class once initiated cannot be changed again
class Person:
    name: str
    address: str
    active: bool = True
    email_address: List[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        """
        If we want to generate a value from the variables that are initialised, then we can use
        this method
        Here after creating the object, we are creating a variable named search_string, which
        generates the values based on the other instance variables
        """
        self._search_string = "Name is {0} Located at {1}".format(self.name, self.address)


person = Person(name='Gowrav', address='123 India')
print(person)

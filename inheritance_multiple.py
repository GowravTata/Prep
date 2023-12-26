"""
Single Inheritance is a property from OOPS, which allows new classes to acquire the properties and methods of
multiple existing classes, the methods from the nearest neighbour are always considered first if the base class
does not have the parent class
"""


class Party:
    party_people = 120

    def __init__(self, people):
        self.people = people

    def attendance(self):
        return f"{self.people} have attended the Party"


class Stadium:
    stadium_people = 12000

    def __init__(self, people, time):
        self.people = people
        self.time = time

    def attendance(self):
        return f"{self.people} have attended the Stadium"


class Arena(Party, Stadium):
    def __init__(self, people):
        super().__init__(people)

    def attendance(self):
        print(super().attendance())  # Ability to use the methods from the parent class
        return f"{self.people} have attended the arena {self.party_people},{self.stadium_people}"


"""
In the child class, if a new object is created, as per the MRO only attribute is needed for the object creation
The number of attributes to the child class should be same as the attributes present to the most near class
if the child class has inherited from multiple classes
"""
event = Arena(1000)
print(event.attendance())

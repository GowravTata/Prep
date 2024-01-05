from dataclasses import dataclass


class Sample:
    def __init__(self, name, age=23):
        self.name = name
        self.age = age

    __private_variable = "Secret"

    def __private_method(self):
        return "Private method called"


obj = Sample('Gowrav', 45)
print(obj.__dict__)


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


@dataclass(kw_only=True)
class RegularCardDC:
    rank: str
    suit: str


queen_of_hearts = RegularCard('Q', 'Hearts')
queen_of_hearts_new = RegularCard('Q', 'Hearts')
print(queen_of_hearts == queen_of_hearts_new)

queen_of_hearts = RegularCardDC('Q', 'Hearts')
queen_of_hearts_new = RegularCardDC('Q', 'Hearts')
print(queen_of_hearts == queen_of_hearts_new)
print(queen_of_hearts)

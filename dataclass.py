from dataclasses import dataclass, field


@dataclass(order=True)
class Investor:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    cash: int = field(repr=True, default=0)

    def __post_init__(self):
        self.sort_index = self.cash


i1 = Investor('Bobby', 27, 700)
i2 = Investor('Tata', 64, 7000)
i3 = Investor('Bobby', 27)

print(i1 < i2)

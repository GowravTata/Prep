"""
Private variables which are defined inside a class can be accessed this way
"""


class Camera:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand


canon = Camera('canon')
print(canon.brand)

canon.brand = 'Nikon'
print(canon.brand)

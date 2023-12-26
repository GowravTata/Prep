"""
Getters Setters can be used to control how the data is accessed or modified
"""
class Car:
    def __init__(self, length):
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length < 4:
            raise ValueError("Under 4 meters cars are not allowed")
        self.__length = length

    def get_length(self):
        """
        We can get the private variable also like this , but this is not the correct way
        """
        return self.__length


vw = Car(4.8)
print(vw.length)

vw.length = 3.9
print(vw.length)

print(Car(4.5).length)

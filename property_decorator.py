"""
This method is used to get or set the attributes of a class, it can be used to access private variables also
This is a method to create a special type of attribute where it can be used to set or get the variable
based on the input that is provided
"""

"""
Here in the below class , if we want to instantiate the class only if the 
"""


class VoterID:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError('Not applicable for Voter ID')
        self.__age = a

    @age.getter
    def age(self):
        return self.__age


numa = VoterID()
numa.age = 13


"""
Interface are the like abstraction which allow strict implementation
"""
from abc import abstractmethod
from zope.interface import Interface


class IFlyable(Interface):
    @abstractmethod
    def fly(self):
        pass


class Airplane(IFlyable):
    def fly(self):
        print("I'm flying!")


class Bird:
    def fly(self):
        print("I'm flying!")



sparrow = Bird()
print(sparrow.fly())

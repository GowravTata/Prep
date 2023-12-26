"""
The property of which allows one to enforce the methods to a class
"""

from abc import ABC, abstractmethod, abstractproperty


class Vehicle(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractproperty
    def model(self):
        pass


class VW(Vehicle):
    def __init__(self):
        self._model = ""

    def name(self):
        return "VW"

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model


polo = VW()
print(polo.name())
print(polo.model)

polo.model = "Porsche"
print(polo.model)

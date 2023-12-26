"""
Method overloading means if a class has multiples methods of the same name and behavior of the method depends
on the input properties , that is known as method overloading, which is not possible in python
If multiple methods are defined in a class, then the method that is defined at last only will be considered.
"""


class Calculator:

    def over_loader(self, a, b=0, c=0):
        output = 0
        if a:
            output = a ** 2
        if a and b:
            output = a + b
        if a and b and c:
            output = a * b * c
        return output


calc = Calculator()
print(calc.over_loader(2))
print(calc.over_loader(2, 3))
print(calc.over_loader(2, 3, 4))

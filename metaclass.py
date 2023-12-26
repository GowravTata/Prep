"""
metaclass is a class that defines how a class behaves, it can be used to customize the class creation
"""


class MetaClass(type):
    def __new__(cls, name, bases, dict):
        dict['new_method'] = lambda self: f"New method added to {name}"
        return super().__new__(cls, name, bases, dict)

    """
    The below is used to create a inbuilt variable from a class
    """
    # def __new__(cls, name, bases, dict):
    #     x = super().__new__(cls, name, bases, dict)
    #     x.country = "India"
    #     return x


class Recipes(metaclass=MetaClass):
    pass


recp = Recipes()

print(recp.new_method())

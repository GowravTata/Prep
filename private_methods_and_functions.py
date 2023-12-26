class Method:
    """
    Private methods are used for the idea of wrapping the data.
    It is used to hide the inner functionality of any class from outside world.
    They can only be accessed inside the class i.e., by the methods present inside the class
    """

    def __init__(self):
        """
        A semi private variable can be called from any class or any object ,
        while a fully private variable cannot be called from any class or any object, it can only be called by the
        methods inside a class
        """

        self._semi_private_variable = "Semi Private Variable"
        self.__fully_private_variable = "Fully Private Variable"

    def __private(self):
        return "private method called"

    def _semi_private(self):
        return "semi private method called"

    def instance_method(self):
        print('From Instance method')
        print(self._semi_private())
        return self.__private()


novo = Method()
print(novo.instance_method())

# A semi private method where it can be called from inside or outside the class
print(novo._semi_private())

print(novo._semi_private_variable)
print(novo.__fully_private_variable)  # This will resilt in a error
# A private method cannot be access inside an object or directly from Class
print(novo.__private())

# A private method can be accessed from outside
print(novo._Method__private())

"""
The below example shows that the protected methods and variables can be accessed from or outside the class
But it is to the programmer that these methods should not be used inside or outside the class
"""


class Laptop:
    def __init__(self, company, ram, memory):
        self._company = company
        self._ram = ram
        self._memory = memory

    def _display_piece(self):
        print("Company", self._company)
        print("Ram", self._ram)
        print("Memory", self._memory)
        return "Buy"


class Dell(Laptop):
    def __init__(self, company, ram, memory):
        super().__init__(company, ram, memory)

    def display_details(self):
        msg = f"Laptop {self._company} , with {self._ram} GB RAM and {self._memory} GB ROM"
        return msg


old_lappy = Laptop('Vostro', 16, 512)
print(old_lappy._display_piece())

new_lappy = Dell('Vostro', 16, 512)
print(new_lappy.display_details())

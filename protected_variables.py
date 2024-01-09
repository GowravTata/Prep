"""
In python , protected variables is a convention to make the variable
protected, while it's main purpose is to hide it's usage
"""


class Biryani:
    _recipe = 'Top Secret'


order = Biryani()
print(order._recipe)

"""
Polymorphism is the ability to do method overloading, method overriding in python
"""


# Method Over Riding

class GrandFather:

    def will(self):
        return "My successor will inherit 1000 acres"


class Father(GrandFather):

    def will(self):
        return "My successor will inherit 100 acres"


class Son(Father):

    def will(self):
        return "My successor will inherit 10 acres"


steve = Son()
print(steve.will())

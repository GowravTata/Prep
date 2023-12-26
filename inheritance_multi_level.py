"""
Inheritance where methods of the base class and derived class are further inherited into a new derived class
"""


class GrandFather:

    def __init__(self, grand_father_name):
        self.grand_father_name = grand_father_name


class Father(GrandFather):
    def __init__(self, father_name, grand_father_name):
        self.father_name = father_name

        GrandFather.__init__(self, grand_father_name)


class Son(Father):
    def __init__(self, son_name, father_name, grand_father_name):
        self.son_name = son_name

        Father.__init__(self, father_name, grand_father_name)

    def print_name(self):
        print('GrandFather name :', self.grand_father_name)
        print("Father name :", self.father_name)
        print("Son name :", self.son_name)


# Driver code
s1 = Son('Philip', 'Charles', 'Willaim')
print(s1.grand_father_name)
print(s1.father_name)
print(s1.son_name)
s1.print_name()

"""
Inheritance involving multiple types of inheritance is called hybrid inheritance
"""


class F:
    def __init__(self):
        print('Class F')


class G:
    def __init__(self):
        print('Class G')


class E(F, G):
    def __init__(self):
        super().__init__()
        print('Class E')


class B(F):
    def __init__(self):
        super().__init__()
        print('Class B')


class A(B):
    def __init__(self):
        super().__init__()
        print('Class A')


class C(B):
    def __init__(self):
        super().__init__()
        print('Class C')


c = C()
e = E()

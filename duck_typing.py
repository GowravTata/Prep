"""
Duck typing is a concept , so that it allows focusing on object's behaviour rather than object type
"""


class Dog:
    @staticmethod
    def sound():
        return "Bow ! Bow !"


class Duck:

    @staticmethod
    def sound():
        return "Quack ! Quack !"


class DuckTyping:
    @staticmethod
    def sound(animal):
        return animal.sound()


dog = Dog()
duck = Duck()

duck_typing = DuckTyping()

print(duck_typing.sound(dog))
print(duck_typing.sound(duck))

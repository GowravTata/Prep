"""
Generator is a type of iterator where it doesn't store the value in the memory, it does all the things in the fly
"""
def create_container(threshold):
    i = 1
    while i < threshold + 1:
        yield i
        i += 1


sets = [i for i in create_container(12)]
print(sets)


def generator_function(limit):
    for i in range(1, limit):
        yield i


gen = generator_function(4)
print(next(gen))
print(next(gen))
print(next(gen))

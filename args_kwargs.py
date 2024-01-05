"""
Script to check the various methods present in args
"""
import sys


def args_checker(*args):
    print(type(args))
    for i in args:
        print(i)
    return


def kwargs_checker(**kwargs):
    print(type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())
    return


print(args_checker('Gowrav', 'Tata'))
print(kwargs_checker(name='Gowrav', age=27, city='Hyderabad'))

print(sys.argv[0])  # This gets the name of the file
# This gets the first argument that is passed from the command line, if nothing is passed index error is raised
print(sys.argv[1])
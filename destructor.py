"""
The method that is called when the instance of the class is deleted
"""


class Folder:
    def __init__(self):
        print('Folder is created')

    def __del__(self):
        print('Folder is deleted')


file = Folder()
del file

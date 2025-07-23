"""
Creating class called "People" with attributes "name" and "age"
"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people_one = People("Francisco", 30)
print(f"{people_one.name} and {people_one.age} age")

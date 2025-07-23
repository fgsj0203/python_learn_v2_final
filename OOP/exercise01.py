"""
Creating class called "People" with attributes "name" and "age"
"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PeopleTwo:
    def __init__(self, firstName, lastName, age, address):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address

other_people = PeopleTwo("Francisco", "junior", 30, "Rua Onze de Fevereiro")
print(f"I {other_people.firstName} with {other_people.lastName} have {other_people.age} and living {other_people.address}")

people_one = People("Francisco", 30)
print(f"{people_one.name} and {people_one.age} age")

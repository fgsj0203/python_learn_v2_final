"""
Creating class with method (leve beginner)
"""


# Creating class with attributes
class People:
    def __init__(self, firstName, lastName, age, address):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address

    # Creating first method for print values
    def printDataPeople(self):
        print(
            f"Hello, I'm {self.firstName} and {self.lastName} with {self.age} and finally living in {self.address}"
        )

    # Creating second method for print data people
    def printAge(self):
        print(f"Hello, i'm have {self.age}")


p1 = People("Francisco", "Junior", 30, "Rua Onze de fevereiro")
p1.printDataPeople()
p1.printAge()

"""
Creating class with attributed dynamic
"""


class People:
    def __init__(self, firstName, lastName, age, colorFavorite, address):
        self.firstName = firstName
        self.LastName = lastName
        self.age = age
        self.colorFavorite = colorFavorite
        self.address = address

    def printData(self):
        print(
            f"{self.firstName} and {self.LastName} have {self.age} and like {self.colorFavorite} and finally living {self.address}"
        )


# Calling class with instance object
p1 = People("Francisco", "Gomes", 30, "Black", "Rua Onze de Fevereiro")
p1.printData()

# Calling attribute dynamic
p1.colorFavorite = "Blue Marine"
p1.printData()

"""
Creating class with value default
"""


class People:
    def __init__(self, name="Francisco", age=30):
        self.name = name
        self.age = age

    def printDataPeople(self):
        print(f"{self.name} and have {self.age} years")


# Creating and instancing object
p1 = People()
p1.printDataPeople()  # Calling method in class

# Attribute dinamic
# -----------------------------------------------------------------
p1.cor = "moreno"  # Attribute dinamic
print(f"{p1.name} have color {p1.cor}")
# -----------------------------------------------------------------

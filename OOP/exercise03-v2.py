"""
Creating version 2.0 of class People with new attributes and methods
"""


class People:
    def __init__(self, firstName, lastName, address, childrens, jobEmployee):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.childrens = childrens
        self.jobEmployee = jobEmployee

    def printNamesValid(self):
        sizeName = len(self.firstName)
        print("The size of name is: %d " % sizeName)
        while sizeName < 3:
            print("Size of name is invalid, try again!")
            name = str(input("Enter with a name: "))
            sizeName = len(name)
        nameReplace = self.firstName.replace(self.firstName, name)
        self.firstName = nameReplace
        print(f"I {self.firstName} with {self.lastName} ")

    def childrenAmountValid(self):
        if self.childrens < 0:
            print("Amount children is invalid, try again!")
            amountChildren = int(input("amount children: "))
        print("The amount of childrens is: %d " % amountChildren)


p1 = People("a", "Gomes", "Rua Onze de Fevereiro", -1, "Software Developer")
p1.printNamesValid()
p1.childrenAmountValid()

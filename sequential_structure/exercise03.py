number_one = int(input("number one: "))
number_two = int(input("number two: "))
print("The sum numbers is: %d" % (number_one + number_two))


# Resolution with function
def sumNumbers(numberOne, numberTwo):
    print(
        "Number one is %d and number two is %d used for calculate sum" % (number_one,
        number_two)
    )
    print("The sum of numbers (with function) %d" % (number_one + number_two))


# Calling function
sumNumbers(10, 15)

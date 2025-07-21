# Function without parameter for validation flow
def number_valid():
    number = int(input("Enter with a number: "))
    while number < 0 or number > 10:
        print("number invalid, try again!")
        number = int(input("Enter again with a number: "))
    print("The number valid is %d \n" % number)


number_valid()

# ---------------------------------------------------------------------------------------------------

# Function with parameter for validation and go flow code


def number_valid_final(number):
    while number < 0 or number > 10:
        print("Function with parameter")
        print("number invalid, try again!")
        number = int(input("What your number: "))

    print("Your number is: %d" % number)


number_valid_final(-1)
# ---------------------------------------------------------------------------------------------------

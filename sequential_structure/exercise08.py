# --------------------------------------------------------------------------------------------------------
number_one = int(input("one: "))
number_two = int(input("two: "))
number_three = float(input("three: "))

operation_one = (number_one * 2) * (number_two / 2)
operation_two = (number_one * 3) + number_three
operation_three = number_three**3

# Printing values final of operations
print("operation one: %.2f" % operation_one)
print("\noperation two: %.2f" % operation_two)
print("\noperation three: %.2f" % operation_three)
# --------------------------------------------------------------------------------------------------------


# Solution with function
def operations_numbers(number_one_function, number_two_function, number_three_function):
    print("\nSolution with function withou validation data")
    operation_one = (number_one_function * 2) * (number_two_function / 2)
    operation_two = (number_one_function * 3) + number_three_function
    operation_three = number_three_function**3

    # Printing values final of operations
    print("operation one: %.2f" % operation_one)
    print("\noperation two: %.2f" % operation_two)
    print("\noperation three: %.2f" % operation_three)


operations_numbers(40, 41, 3.14)
# --------------------------------------------------------------------------------------------------------


# Solution with validation of data input user
def operations_numbers_valid(number_one_valid, number_two_valid, number_three_valid):
    print("Solution with validation data user input")
    while number_one_valid < 0:
        print("number invalid, try again!")
        number_one_valid = int(input("number one: "))
    while number_two_valid < 0:
        print("number invalid, try again!")
        number_two_valid = int(input("number two: "))
    while number_three_valid < 0:
        print("number invalid, try again!")
        number_three_valid = float(input("number three: "))
    operation_one = (number_one_valid * 2) * (number_two_valid / 2)
    operation_two = (number_one_valid * 3) + number_three_valid
    operation_three = number_three_valid**3

    # Printing values final of operations
    print("operation one: %.2f" % operation_one)
    print("\noperation two: %.2f" % operation_two)
    print("\noperation three: %.2f" % operation_three)

operations_numbers_valid(-1,3,-2)
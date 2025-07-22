list_five_numbers = []

for x in range(0, 5):
    number = int(input())
    list_five_numbers.append(number)

print("The list of numbers is: ", list_five_numbers)


# Using functions
def list_numbers():
    list_function_numbers = []
    for x in range(0, 5):
        number = int(input())
        list_function_numbers.append(number)
    print("*** Final list of numbers ***")
    print(list_function_numbers)


# Calling function
list_numbers()

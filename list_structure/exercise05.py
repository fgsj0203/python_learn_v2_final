"""
Return get largest number in list
"""

list_numbers_bigger = []
bigger_number = 0
for x in range(0, 5):
    number = int(input("number: "))
    list_numbers_bigger.append(number)

for x in list_numbers_bigger:
    if x > bigger_number:
        bigger_number = x
    else:
        x = x

print(bigger_number)


# Creating solution with function
def bigger_number(list_numbers):
    number_aux = 0
    for x in list_numbers:
        if x > number_aux:
            number_aux = x

    print("The bigger number %d " % number_aux)


bigger_number([1, 2, 4, 18, 9, 0])

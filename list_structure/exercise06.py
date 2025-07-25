smaller_number = 0
list_numbers = []

for x in range(0, 5):
    number = int(input("number: "))
    list_numbers.append(number)

for i in list_numbers:
    if i < smaller_number:
        smaller_number = i

print(smaller_number)


# Solution with function and parameter
def smaller_number(list_smaller_numbers):
    number_smaller = 0
    number_list = []
    for x in number_list:
        if x < number_smaller:
            number_smaller = x
    print(number_smaller)


smaller_number([1, 5, 3, 4, 9, 0])
# --------------------------------------------------------

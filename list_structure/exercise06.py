smaller_number = 0
list_numbers = []

for x in range(0, 5):
    number = int(input("number: "))
    list_numbers.append(number)

for i in list_numbers:
    if i < smaller_number:
        smaller_number = i

print(smaller_number)

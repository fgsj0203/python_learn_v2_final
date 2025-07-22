list_total_numbers = []
list_numbers_pair = []
list_numbers_odd = []

for x in range(0, 5):
    number = int(input("Number: "))
    list_total_numbers.append(number)
    if number % 2 == 0:
        list_numbers_pair.append(number)
    else:
        list_numbers_odd.append(number)

print("List with total numbers: ", list_total_numbers)
print("List numbers pair: ", list_numbers_pair)
print("List numbers odd: ", list_numbers_odd)

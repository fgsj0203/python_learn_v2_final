def operation_numbers_interval(number_one, number_two):
    list_numbers = []
    sum_numbers = 0
    for x in range(number_one, number_two):
        print(x)
        list_numbers.append(x)
    for x in list_numbers:
        sum_numbers += x
    print("The sum of numbers is: %d " % sum_numbers)


operation_numbers_interval(1, 10)

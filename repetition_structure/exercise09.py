def generate_table_numbers(number):
    for x in range(1, number + 1):
        print("%d X %d = %d" % (x, number, (x * number)))


generate_table_numbers(10)

number_one = int(input("number one: "))
number_two = int(input("number two: "))
if number_one > number_two:
    print("The number one is %d is bigger" % number_one)
else:
    print("The number two is %d is bigger" % number_two)


# Solution with function


def bigger_number(number_one, number_two):
    if number_one > number_two:
        print("The number one is %d is bigger" % number_one)
    else:
        print("The number two is %d is bigger" % number_two)


bigger_number(-10, 5)

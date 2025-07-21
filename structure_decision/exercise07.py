# --------------------------------------------------------------------------
day_week = int(input("Input day of week with number 1-7: \n"))

if day_week == 1:
    print("Sunday")
elif day_week == 2:
    print("Monday")
elif day_week == 3:
    print("Tuesday")
elif day_week == 4:
    print("Wednesday")
elif day_week == 5:
    print("Thursday")
elif day_week == 6:
    print("Friday")
elif day_week == 7:
    print("Saturday")
else:
    print("Day invalid, try again!")
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Function with validation field data


def day_week(number_day):
    while number_day <= 0 or number_day > 7:
        print("Number day is invalid, try again!")
        number_day = int(input("Input day of week with number 1-7: \n"))
        if number_day == 1:
            print("Sunday")
        elif number_day == 2:
            print("Monday")
        elif number_day == 3:
            print("Tuesday")
        elif number_day == 4:
            print("Wednesday")
        elif number_day == 5:
            print("Thursday")
        elif number_day == 6:
            print("Friday")
        elif number_day == 7:
            print("Saturday")


# Testing with number day value 10 (forced value not valid)
day_week(10)
# --------------------------------------------------------------------------

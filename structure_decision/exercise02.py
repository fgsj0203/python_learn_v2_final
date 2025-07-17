# ------------------------------------------------------------------------------------
number = int(input("number: "))

if number >= 0:
    print("number is positive: %d" % number)
else:
    print("Number is negative: %d" % number)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
def number_value(number):
    print("\n*** Solution with function ***")
    if number >= 0:
        print("number is positive: %d" % number)
    else:
        print("number is negative: %d" % number)


number_value(10)
# ------------------------------------------------------------------------------------

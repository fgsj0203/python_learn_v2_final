# --------------------------------------------------------------------------------------------------
height_people = float(input("height of people: "))
# Calculate weight ideal with base data height of people
weight_ideal = (72.7 * height_people) - 58

print("The weight ideal with base %.2f is %.2f Kg" % (height_people, weight_ideal))
# --------------------------------------------------------------------------------------------------


# Solution with function without validation data
def weight_ideal(height_people_function):
    print("\nSolution with function")
    weight_ideal_function = (72.7 * height_people_function) - 58
    print(
        "The weight ideal for people with %.2f is %.2fkg"
        % (height_people_function, weight_ideal_function)
    )


weight_ideal(1.81)
# --------------------------------------------------------------------------------------------------


# Solution with function and validation data
def weight_ideal_validation(height_people):
    print("*** Solution with function and validation data ***")
    while height_people <= 0:
        print("Height invalid, try again!")
        height_people = float(input("What height of people: "))
    weight_ideal_people = (72.7 * height_people) - 58
    print("The weight ideal for people is: %.2f KG " % weight_ideal_people)


weight_ideal_validation(-10)

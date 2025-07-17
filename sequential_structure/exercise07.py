side_square = float(input("Size of side square: "))
area_square = side_square * side_square
print("The value of side square with %.1f is area %.2f" % (side_square, area_square))
print("\nThe value double of result area square is: %.2f " % (area_square * 2))


# Solution with function
def area_square_function(side_square_function):
    print("\nSolution with function")
    area_square_function = side_square_function * side_square_function
    print("\nThe value of area square is %.2f " % area_square_function)
    print(
        "\nThe value double of result previous of square is: %.2f "
        % (area_square_function * 2)
    )


# Calling function
area_square_function(3)


# Solution with function and validation data
def area_square_validation(side_square_validation):
    print("\nSolution with validation data")
    while side_square_validation < 0:
        print("\nvalue of side is invalid, try again!")
        side_square_validation = float(input("New value and valid of side square: "))
    area_square_valid = side_square_validation * side_square_validation
    print("\nThe value of area square is: %.2f " % area_square_valid)
    print(
        "\nThe value double of original result square is: %.2f "
        % (area_square_valid * 2)
    )


area_square_validation(-1)

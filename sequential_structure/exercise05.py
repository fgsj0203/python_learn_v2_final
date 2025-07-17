meters_size = int(input("What size in meters: "))
converter_meters_centimeters = meters_size * 100
print("The %d meters is %d centimeters" % (meters_size, converter_meters_centimeters))


# Solution with function
# ---------------------------------------------------------
def converterSize(meters_size):
    converter = meters_size * 100
    print(
        "The size meters %d is converted %d centimeters (solution with function)"
        % (meters_size, converter)
    )

converterSize(5)
# ---------------------------------------------------------

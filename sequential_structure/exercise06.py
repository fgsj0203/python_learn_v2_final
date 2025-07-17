PI = 3.14159
raid_circle = float(input("raid of circle: "))
formula_area_circle = PI * (raid_circle**2)
print("The area of circle is: %.3f" % formula_area_circle)


# -------------------------------------------------------------------------------------
# Solution with function
def area_circle(raid_circle):
    print("Solution with function")
    formula_area_circle = PI * (raid_circle**2)
    print("The area of circle is: %.3f" % formula_area_circle)


area_circle(1)
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# Solution with function and validation data
def area_circle_validation(raid_circle):
    print("Solution with validation")
    while raid_circle < 0:
        print("Value of raid invalid, try again!")
        raid_circle = float(input("new value of raid circle: "))

    formula_area_circle = PI * (raid_circle**2)
    print("The area of circle is: %.3f" % formula_area_circle)


area_circle_validation(-1)
# -------------------------------------------------------------------------------------

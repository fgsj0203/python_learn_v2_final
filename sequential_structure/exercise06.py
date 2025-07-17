PI = 3.14159
raid_circle = float(input("raid of circle: "))
formula_area_circle = PI * (raid_circle**2)
print("The area of circle is: %.3f" % formula_area_circle)


# Solution with function
def area_circle(raid_circle):
    print("Solution with function")
    formula_area_circle = PI * (raid_circle**2)
    print("The area of circle is: %.3f" % formula_area_circle)


area_circle(1)

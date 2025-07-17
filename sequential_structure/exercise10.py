height_people = float(input("Height of people: "))

weight_ideal_man = (72.7 * height_people) - 58
weight_ideal_women = (62.1 * height_people) - 44.7

# printing values of weight ideal for man and women
print(
    "The weight ideal for man is %.2f kg \nand weight ideal for women is %.2f kg "
    % (weight_ideal_man, weight_ideal_women)
)


# Solution with function without validation data
def weight_ideal_people(height_people):
    print("***** Solution with function and without validation data *****")
    weight_ideal_function_man = (72.7 * height_people) - 58
    weight_ideal_function_women = (62.1 * height_people) - 44.7

    print(
        "The weight ideal for man is %.2f kg \nand weight ideal for women is %.2f kg"
        % (weight_ideal_function_man, weight_ideal_function_women)
    )


weight_ideal_people(1.90)

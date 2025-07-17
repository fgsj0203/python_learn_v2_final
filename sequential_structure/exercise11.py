# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
TAX_PRICE = 4.00
weight_fish = float(input("Weight fish: "))

if weight_fish > 50:
    print("Your have payment tax under weight fish")
    tax_payment = (weight_fish - 50) * TAX_PRICE
    print(
        "The excess weight of table isent weight of fish is %.1f kg You payment of tax under weight fish is: R$ %.2f "
        % ((weight_fish - 50), tax_payment)
    )

else:
    print("You is isent of payment")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Solution with function
def tax_payment_condition(weight_fish):
    print("\n***** Solution with function *****")
    if weight_fish > 50:
        tax_payment_value = (weight_fish - 50) * TAX_PRICE
        print(
            "The excess weight fish is bigger under table of values isent in %.1f and you payment of tax under weight fish is: %.2f"
            % ((weight_fish - 50), tax_payment_value),
        )
    else:
        print("You isent of payment tax under weight fish excess")


tax_payment_condition(55)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Solution with validation data
def tax_payment_valid(weight_fish):
    while weight_fish <= 0:
        print("Weight invalid, number negative, try again!")
        weight_fish = float(input("What weight fish: "))
    if weight_fish <= 50:
        print("You isent of payment tax of weight")
    else:
        tax_payment_value = (weight_fish - 50) * TAX_PRICE
        print(
            "The excess weight fish is bigger under table of values in %.1f kg and you payment of tax under weight is %.2f"
            % ((weight_fish - 50), tax_payment_value)
        )


tax_payment_valid(-10)

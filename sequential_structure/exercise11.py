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

# --------------------------------------------------------------------
for x in range(0, 21):
    print(x)

for x in range(0, 21):
    print(x, end=" ")

# Solution using function for two formats


# --------------------------------------------------------------------
def number_under():
    for x in range(0, 21):
        print(x)


def number_side():
    for x in range(0, 21):
        print(x, end=" ")


# --------------------------------------------------------------------

# Calling functions

print("\n********* Printing value final ***********")
number_under()
number_side()

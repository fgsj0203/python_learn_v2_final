"""
Calculate string lenght
"""

string = str(input("string: "))
size_string = len(string)
print("The size of string is: %d" % size_string)


# -----------------------------------------------------------
"""
Creating solution without function builtin len()
"""


def sizeString(str1):
    count_string = 0

    for x in str1:
        count_string += 1

    return count_string


print(sizeString("francisco"))
# -----------------------------------------------------------

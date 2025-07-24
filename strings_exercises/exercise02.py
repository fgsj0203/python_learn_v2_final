"""
return two firsts characters and two last characters
"""


def returnString(str_one):
    size_string = len(str_one)
    if size_string < 2:
        print("String empty")
    elif size_string == 2:
        print((str_one[0] + str_one[1]) * 2)
    elif size_string > 2:
        print((str_one[0] + str_one[1]) + (str_one[-2] + str_one[-1]))


returnString("francisco")
returnString("fr")
returnString("f")

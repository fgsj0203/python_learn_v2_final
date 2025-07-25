"""
Exercise: Reverse word
"""

string_name = str(input("string: "))
print(
    "The string original %s in order reverse is %s" % (string_name, string_name[::-1])
)


# -------------------------------------------------------------------
# Solution using function without parameter
def reverse_string():
    name = str(input("string: "))
    print("original: %s" % name)
    print("reverse order: %s" % name[::-1])


reverse_string()
# -------------------------------------------------------------------


# Solution using function with parameter
def string_reverse(string1):
    print("\n------- Final reverse --------")
    print("original: %s" % string1)
    print("reverse: %s" % string1[::-1])


string_reverse("francisco")
# -------------------------------------------------------------------

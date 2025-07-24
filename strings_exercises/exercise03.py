string_one = str(input("string: "))

# string.replace(string_one)
for x in string_one:
    char_replace = string_one[0]
    for i in string_one:
        if i == char_replace:
            string_one[i].replace("$")

    print(string_one)

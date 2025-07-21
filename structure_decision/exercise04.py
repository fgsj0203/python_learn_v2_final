# ------------------------------------------------------------------
letter = str(input("Input your letter: "))
if letter not in ("a", "e", "i", "o", "u"):
    print("The letter is consonant")
else:
    print("The letter is vowel")
# ------------------------------------------------------------------


# ------------------------------------------------------------------
def identify_letter(letter):
    if letter not in ("a", "e", "i", "o", "u"):
        print("The letter is consonant")
    else:
        print("The letter is vowel")


identify_letter("a")
# ------------------------------------------------------------------

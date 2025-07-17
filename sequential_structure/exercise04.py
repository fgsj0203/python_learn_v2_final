# first form resolution problem without validation data
note_one = float(input("note one: "))
note_two = float(input("note two: "))
note_three = float(input("note three: "))
note_four = float(input("note four: "))
average_notes = (note_one + note_two + note_three + note_four) / 4.0
print("The average notes is: %.1f" % average_notes)

# Second form resolution problem with validation data
# Using structure condition with "while"
note_one = float(input("note one: "))
while note_one > 10 or note_one < 0:
    print("Note invalid, try again!!")
    note_one = float(input("note one: "))

note_two = float(input("note two: "))
while note_two > 10 or note_two < 0:
    print("Note invalid, try again!!")
    note_two = float(input("note two: "))

note_three = float(input("note three: "))
while note_three > 10 or note_three < 0:
    print("Note invalid, try again!!")
    note_three = float(input("note three: "))

note_four = float(input("note four: "))
while note_four > 10 or note_four < 0:
    print("Note invalid, try again!!")
    note_four = float(input("note four: "))

average_notes = (note_one + note_two + note_three + note_four) / 4.0

print("The average of notes is: %.1f" % average_notes)


# ------------------------------------------------------------------------------------------
# Solution with function
def averageNotes(note_one, note_two, note_three, note_four):
    # note_one = float(input("note one: "))

    while note_one > 10 or note_one < 0:
        print("Note invalid, try again!!")
        note_one = float(input("note one: "))

    # note_two = float(input("note two: "))
    while note_two > 10 or note_two < 0:
        print("Note invalid, try again!!")
        note_two = float(input("note two: "))

    # note_three = float(input("note three: "))
    while note_three > 10 or note_three < 0:
        print("Note invalid, try again!!")
        note_three = float(input("note three: "))

    # note_four = float(input("note four: "))
    while note_four > 10 or note_four < 0:
        print("Note invalid, try again!!")
        note_four = float(input("note four: "))

    average_notes = (note_one + note_two + note_three + note_four) / 4.0

    print("The average of notes is: %.1f " % average_notes)

    averageNotes(12, 13, 9, 8)

# ------------------------------------------------------------------------------------------

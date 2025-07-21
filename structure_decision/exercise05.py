# --------------------------------------------------------------------
# Calculating average of two notes without validation data
note_one = float(input("note one: "))
note_two = float(input("note two: "))

average_notes = (note_one + note_two) / 2.0

print("The average of two notes is %.2f " % average_notes)

if average_notes > 10.0:
    print("Average invalid")
elif average_notes == 10.0:
    print("Approved with distinction")
elif average_notes >= 7.0 or average_notes <= 9.9:
    print("Approved")
else:
    print("Reproved")

# --------------------------------------------------------------------


# --------------------------------------------------------------------
# Calculate average of two notes with validation data
def validation_average_notes(note_one, note_two):
    while note_one < 0 or note_one > 10:
        print("Note invalid, try again!")
        note_one = float(input("note one: "))
    while note_two < 0 or note_two > 10:
        print("Note invalid, try again!")
        note_two = float(input("note two: "))
    average_notes = (note_one + note_two) / 2.0
    if average_notes == 10.0:
        print("Approved with distinction")
    elif average_notes >= 7.0 and average_notes <= 9.9:
        print("Approved")
    else:
        print("Reproved")


validation_average_notes(9, 8)

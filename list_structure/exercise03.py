def average_notes_lists():
    list_notes = []
    sum_notes = 0
    for x in range(0, 4):
        note = float(input("note: "))
        list_notes.append(note)
        sum_notes += note

    average_notes = sum_notes / 4.0
    print("List original numbers: ", list_notes)
    print("The average of notes: ", average_notes)


average_notes_lists()

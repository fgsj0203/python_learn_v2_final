gender_people = str(input("Gender people: F ou M \n"))
gender_people_first_letter = gender_people[0].lower()

if gender_people_first_letter == "f":
    print("Female")
elif gender_people_first_letter == "m":
    print("Male")
else:
    print("Gender invalid")

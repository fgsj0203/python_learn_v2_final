# Validation withou function

name_people = str(input("Name people: "))
while len(name_people) <= 3:
    print("Name is small, name need most 3 characters")
    name_people = str(input("Name people (validation): "))

age_people = int(input("Age of people: "))
while age_people < 0 or age_people > 150:
    print("Age invalid, try again!")
    age_people = int(input("Age people (validation): "))

salary = float(input("Your salary: "))
while salary < 0:
    print("Salary invalid, try again!")
    salary = float(input("Salary (validation): "))

gender_people = str(input("Your gender: \n"))
while gender_people[0].lower() not in ("f", "m"):
    print("Gender invalid, try again!")
    gender_people = str(input("Your gender (validation): "))

state_civil = str(input("Your state civil: \n"))
while state_civil[0].lower() not in ("s", "c", "v", "d"):
    print("State civil invalid, try again!")
    state_civil = str(input("State civil (validation): "))

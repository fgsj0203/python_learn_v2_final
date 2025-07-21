name_user = str(input("Name user: "))
password_user = str(input("Password: "))


while name_user == password_user:
    print("Name and password is equal, change name or password")
    name_user = str(input("Name user: "))
    password_user = str(input("Password: "))

print("------------------ Print final -------------------")
print("\nResult public final\n")
print("Your name user is: %s " % name_user)
print("Your password is: %s " % password_user)

name_user = str(input("Name user: "))
password_user = str(input("Password: "))


while name_user == password_user:
    print("Name and password is equal, change name or password")
    name_user = str(input("Name user: "))
    password_user = str(input("Password: "))

print("------------------ Print final -------------------")
print("Your name user is: %s " % name_user)
print("Your password is: %s " % password_user)
print("------------------ Print final -------------------")

# ---------------------------------------------------------------------------------------------


# Creating function with parameter
def validation_password_user(name_user, password):
    while name_user == password:
        print("Solution with parameters \n")
        print("name and password is equal, change values")
        name_user = str(input("Name user: "))
        password = str(input("Password: "))
    print("\nResult final \n")
    print(name_user)
    print(password)


# Calling function with paramter
validation_password_user("francisco", "francisco")

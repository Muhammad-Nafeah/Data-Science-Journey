# Write a program that takes an age variable
# Print "Child" if age is below 13
# Print "Teenager" if age is between 13 and 17
# Print "Adult" if age is between 18 and 59
# Print "Senior" if age is 60 or above
# Test with ages: 8, 15, 25, 65


def AgeChecker(age):
    if age < 13:
        print("Child")
    elif age >= 13 and age <=17:
        print("Teenager")
    elif age >= 18 and age <= 59:
        print("Adult")
    elif age >= 60:
        print("Senior")
    else:
        print("Invalid age")

AgeChecker(13)
AgeChecker(17)
AgeChecker(18)
AgeChecker(59)



# Store a correct username and password in variables
# Store an entered username and password in variables
# If both match — print "Login Successful"
# If username matches but password is wrong — print "Wrong Password"
# If username is wrong — print "User Not Found"


user_name = "Nafeah"
password = "qwerty123"

def LoginChecker(username_input, password_input):
    if username_input == user_name and password_input == password:
        print("Login successful")
    else:
        print("Login failed")
        print("Please check your username and password and try again.")

LoginChecker("Nafeah", "qwerty123")
LoginChecker("Nafeah", "wrongpassword")
LoginChecker("WrongUsername", "qwerty123")


# Write a function called electricity_bill(units)
# First 100 units: 5 rupees per unit
# Next 100 units (101-200): 8 rupees per unit
# Above 200 units: 12 rupees per unit
# Print the total bill
# Test with: 80, 150, 250 units


def ElectricityBill(units):

    if (units <= 100):
        per_unit_cost = 0.5
    elif (units > 100 and units <= 200):
        per_unit_cost = 8
    elif (units > 200):
        per_unit_cost = 12
    else:
        print("Invalid input")
        return
    total_bill = units * per_unit_cost
    print(f"Total electricity bill for {units} units is: {total_bill}")

ElectricityBill(50)
ElectricityBill(150)
ElectricityBill(250)



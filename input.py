# input() = A function that prompts the user to enter data
#           Returns the entered data as a string


name = input("What is your name ")

print(f"{name} is you full name")

age = input("What's your age:? ")
formattedAge = int(age)
formattedAge += 1
print(type(formattedAge))
print("HAPPY BIRTHDAY")
print(f"You are {formattedAge} years old")

# Check ifIsBirthday
""" age = int(input("What\'s your age "))
birthMonth = input("Enter your birth month")
birthDate = int(input("Enter your birth date").capitalize())
birthYear = int(input("Enter your birth year"))

if age == 25 and birthMonth == "November" and birthDate == 19:
    print("HAPPY BIRTHDAY 🎂🎂")
    print(f"You are {2025 - birthYear} years old ")
else:
    print("Sorry today is not your birthday") """

# Exercise 1

width = float(input("What's the width: "))
length = float(input("What's the length: "))
area_of_rectangle = width * length
print(f"The area of the rectangle is {area_of_rectangle}cm^2")
# Exercise 2
# item
# price
# quantity

item = input("What item would you like to buy today? ")
price = float(input("What's the price? "))
quantity = float(input("How many would you like to have in total? "))

print(f"Here is your {item} the total price is ${quantity * price}")

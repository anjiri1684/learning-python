# if = Do some code only of some condition is True
#      else do something else

age = int(input("Enter you age: "))
referred = False
response = input("Would you like food? (Y?N): ")

if response.lower() == "y":
    print("We are serving you in a few")
elif response.lower() == 'n':
    print("It's okay maybe next time")
else:
    print("You are advised to choose between n for no and y for yes")


if age >= 18 or referred:
    print("You are allowed to signup for these services")
elif age < 0:
    print("Enter age equal or greater than 1")
else:
    print("I'm sorry you can't be signed for this service")

name = input("Enter your name")

if name.strip() == "":
    print("You have entered nothing please enter a valid name")
else:
    print(f"Hello {name}")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

# conditions expression = A one line shortcut for the if - else statement(ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

sunny = False
print("It is sunny" if sunny else "It is cold")

num = 6
result = "Even" if num % 2 == 0 else "Odd"
print(result)

name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")
result = len(name)
result = name.find("v")
result = name.rfind('q')
result = name.capitalize()
result = name.upper()
result = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count('-')
result = phone_number.replace('-', "")
print(result)
print(help(str))

checkValidEmail = input("Enter your email: ")

username = input("Enter your username")

if len(username) > 12 or len(username) < 4 or " " in username or not username.isalpha():
    print("Invalid username")

else:
    print(f"Welcome {username}")
    userEmail = input("Enter your Email address")
    if "@" in userEmail:
        print(f"{username} your email is {userEmail}")
    else:
        print(f"{username} Please enter a valid email")
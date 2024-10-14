# This is my first python program
# print("I like pizza!")
# print("It's really good!")

# Variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains

# strings
""" first_name = 'Vincent'
last_name = "Anjiri"
email = "vincentanjiri12@gmail.com"
print(first_name + " " + last_name)

print(f"Hello {first_name} {last_name}")
print(f"Hello this is {first_name} you can contact me via my personal email {email}") """

# Integers
"""age = 24
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")"""

# floats
"""price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You run {distance}km")"""

# booleans
"""is_student = True
for_sale = False
is_online = False
# print(f"Are you a student? : {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not for sale")

if is_online:
    print("You are online")
else:
    print("You are offline")"""

# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

"""  name = "Vincent Anjiri"
age = 24
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
age = float(age)
age = str(age)
name = bool(name)
print(gpa)
print(age)
print(type(age))
print(name)  """

# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

"""  name = input("What is your name ")

print(f"{name} is you full name")

age = input("What's your age:? ")
formattedAge = int(age)
formattedAge += 1
print(type(formattedAge))
print("HAPPY BIRTHDAY")
print(f"You are {formattedAge} years old")  """

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

"""  width = float(input("What's the width: "))
length = float(input("What's the length: "))
area_of_rectangle = width * length
print(f"The area of the rectangle is {area_of_rectangle}cm^2")  """

# Exercise 2
# item
# price
# quantity

"""  item = input("What item would you like to buy today? ")
price = float(input("What's the price? "))
quantity = float(input("How many would you like to have in total? "))

print(f"Here is your {item} the total price is ${quantity * price}")  """

# Exercise 3
# mad libs game
# word game where you create a story by filling in blanks with random words

"""  adjective1 = input("Enter an adjective (description of something)")
noun1 = input("Enter a noun (person, place, thing)")
adjective2 = input("Enter an adjective (description of something) ")
verb1 = input("Enter a verb ending with a 'ing'(a doing word) ")
adjective3 = input("Enter an adjective")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")  """

# Arithmetic operations
# friends = 50
# friends += 1
# friends -= 2
# friends *= 3
# friends /= 2
# friends **= 2
#
# friends %= 4
#
# print(friends)

# Math functions
# x = 3.14
# y = 4
# z = 5
#
# # results = round(x)
# # results = abs(y)
# # results = pow(y, 3)
#
# results = max(x,y,z)
# # results = min(x,y,z)
# print(results)

# import math

# x = 9 + 0.5
# print(math.pi)
# print(math.e)
# results = math.sqrt(x)
# results = math.ceil(x)
# print(results)

# calPi = math.pi

# radius = float(input("Enter the radius "))
# circumference = 2 * calPi * radius
# circumference = round(circumference, 2)
# print(f"The Circumference is {circumference}cm^2")
# area_of_circle = calPi * (radius ** 2)
# area_of_circle = round(area_of_circle, 3)
# print(f"The calculated area of the circle is {area_of_circle}cm^2")

# calculating the area of hypotenuse triangle

# length = float(input("Enter the length "))
# width = float(input("Enter the width "))
# side = math.sqrt(pow(length, 2) + pow(width, 2))
# side = round(side, 3)
# print(f"The calculated area is {side}cm^2")

# if = Do some code only of some condition is True
#      else do something else

# age = int(input("Enter you age: "))
# referred = False
# response = input("Would you like food? (Y?N): ")
#
# if response.lower() == "y":
#     print("We are serving you in a few")
# elif response.lower() == 'n':
#     print("It's okay maybe next time")
# else:
#     print("You are advised to choose between n for no and y for yes")


# if age >= 18 or referred:
#     print("You are allowed to signup for these services")
# elif age < 0:
#     print("Enter age equal or greater than 1")
# else:
#     print("I'm sorry you can't be signed for this service")

# name = input("Enter your name")
#
# if name.strip() == "":
#     print("You have entered nothing please enter a valid name")
# else:
#     print(f"Hello {name}")

# for_sale = True
#
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")


# Simple calculator
"""  operator = input("Choose between + - / * ")

if operator == "+" or operator == "-" or operator == "*" or operator == '/':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        result = num1 / num2
        print(round(result, 3))
else:
    print("Enter a valid mathematical operator")  """

# Python weight converter

"""  unit = input("Enter your unit kg or l: ")

if unit == 'l' or unit == 'kg':
    weight = float(input("Enter your weight: "))
    if unit == 'kg':
        weight *= 2.205
        unit = 'Lbs'
        print(f"Your unit is {round(weight, 2)} {unit}")
    elif unit == 'l':
        weight /= 2.205
        unit = 'kg'
        print(f"Your unit is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is an invalid unit")  """

"""  unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

if (unit == 'c' or unit == "C") or (unit == 'f' or unit == 'F'):
    temp = float(input("Enter the temperature: "))
    if unit == 'c':
        result = round((9 * temp) / 5 + 32, 1)
        print(f"The temperature in Fahrenheit is: {result}^F")
    else:
        result = round((temp - 32) * 5 / 9, 1)
        print(f"The temperature in Celsius is: {temp}^C")
else:
    print(f"{unit.upper()} is not a valid unit")  """

# logical operators = evaluate multiple conditions (or, and , not)
#                     or = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the condition (not False, not True)


# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor is still scheduled")


# temp = 30
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is hot outside🥵")
#     print("Its sunny ☀️")
# elif temp <= 0 and is_sunny:
#     print('It is Cold outside 🥶')
#     print("Its sunny ☀️")
# elif 28 > temp < 0 and is_sunny:
#     print('It is warm outside 🥴')
#     print("Its sunny ☀️")

# print(not is_sunny)


# conditions expression = A one line shortcut for the if - else statement(ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

# sunny = False
# print("It is sunny" if sunny else "It is cold")
#
# num = 6
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")
# result = len(name)
# result = name.find("v")
# result = name.rfind('q')
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count('-')
# result = phone_number.replace('-', "")
# print(result)
# print(help(str))

# checkValidEmail = input("Enter your email: ")

# username = input("Enter your username")
#
# if len(username) > 12 or len(username) < 4 or " " in username or not username.isalpha():
#     print("Invalid username")
#
# else:
#     print(f"Welcome {username}")
#     userEmail = input("Enter your Email address")
#     if "@" in userEmail:
#         print(f"{username} your email is {userEmail}")
#     else:
#         print(f"{username} Please enter a valid email")


# indexing = accessing elements of a sequence using [] (indexing operators)
# [start : end: step ]

# credit_number = "1234-5678-9012-3456"
# print(credit_number[0:4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])
# last_digits = credit_number[-5:]
# credit_number = credit_number[::-1]
# print(credit_number)

# format specifiers = {value: flags} format value based on what flags are inserted

# price1 = 30000.14159
# price2 = -90087.65
# price3 = 1200.34
#
# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")

# while loops = execute some code while some condition remain true

# name = input("Enter your name")

# while name == '':
#     print("You did not enter your name")
#     name = input("Enter your name")
# print(f"Hello {name}")


# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Invalid age")
#     age = int(input("Enter your age: "))
# if age == 0:
#     print("Age can't be 0")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old")


# food = input("Enter your favorite food (q to quit)")
#
# while not food == 'q':
#     food = input("Enter your favorite food (q to quit)")
#     if len(food) > 3:
#         food = input("Enter your favorite food (q to quit)")
#     print(f"You like {food}")
# print("Bye")

# num = int(input("Enter a number between 1 - 10"))
#
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1 - 10"))
#
# print(f"Your number is {num}")

# Python compound interest calculator
"""   principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to 0")

while rate <= 0:
    rate = float(input("Enter the interest rate amount: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to 0")

while time <= 0:
    time = int(input("Enter the  time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to 0")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: {total:.2f}")   """

# for loops = execute a block of code a fixed number of times.
# you can iterate over a range, strings, sequence, etc


# for x in reversed(range(1)):
#     print(x)
#
# print("HAPPY NEW YEAR")


# credit_card = '1234-5678-9012-3456'
#
# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 3:
#         break
#     else:
#         print(x)


# import time
#
# my_time = int(input("Enter the time in seconds"))
#
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("TIMES UP")


# nested loops = A loop within another loop (outer, inner)
# outer loop
# inner loop

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")
#
# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print("")

# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates Ok
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

# fruits = ["apple", "banana", "orange", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[-1] = "pineapple"

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "avocado")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
# for fruit in fruits:
#     print(fruit)

# fruits = {"apple", "banana", "orange", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
#
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits = ("apple", "banana", "orange", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("apple"))
#
# for fruit in fruits:
#     print(fruit)
#
# print(fruits)

# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)
#
# print("------- YOUR CART -----")
#
# for food in foods:
#     print(food, end="")
#
# for price in prices:
#     total += price
# print("-----------------------")
# print(f"Your total is: ${total}")


# fruits = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'mango', 'pineapple', 'kiwi', 'peach', 'pear']
#
# vegetables = ['carrot', 'broccoli', 'spinach', 'tomato', 'cucumber', 'lettuce', 'bell pepper', 'onion', 'potato']
#
# meat = ['chicken', 'beef', 'pork', 'lamb', 'turkey', 'salmon', 'tuna', 'shrimp', 'duck', 'venison']
#
# groceries = [fruits, vegetables, meat]
# print(groceries[0])

# num_pad = (
#             (1,2,3),
#             (4,5,6),
#             (7,8,9),
#             ("*",0,"#"))
#
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# Python quiz game


# questions = (
#     "How man elements are in the periodic table: ",
#     "Which animal lays the largest eggs?: ",
#     "What is the most abundant gas in Earth's atmosphere?: ",
#     "How many bones are in the human body?: ",
#     "Which planet in the solar system is the hottest?: ")
#
# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#            ("A. 206", "B. 207", "C. 208", "D. 209"),
#            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
#
# question_num = 0
#
# for question in questions:
#     print("-------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input("Enter (A, B, C, D)").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct")
#     else:
#         print("Incorrect")
#         print(f"{answers[question_num ]} is the correct answer")
#     question_num += 1
#
#
# print("-------------------------")
# print("          RESULTS        ")
# print("-------------------------")
#
# print("answers", end=" ")
# for answer in answers:
#     print(answer, end=" ")
#
# print()
#
# for guess in guesses:
#     print(guess, end=" ")
#
# print()
#
# score = int(score / len(questions) * 100)
# print(f"Your score is {score}%")


# dictionary = a collection of {key:value}pairs
#              ordered and changeable. No duplicates

# capitals = {"USA": "Washington D.C",
#             "India": "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow",
#             "Kenya": "Nairobi"}


# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))


# if capitals.get("Kenya"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# values = capitals.values()
# for key in keys:
#     print(key)
#
# print()
#
# for value in values:
#     print(value)

# items = capitals.items()
# print(items)

# for key, value in capitals.items():
#     print(f"{key} ===== {value}")


# concession stand program


# dictionary {key:value}


# menu = {"pizza": 3.00,
#         "nachos": 4.50,
#         "popcorn": 6.00,
#         "fries": 2.50,
#         "chips": 1.00,
#         "pretzel": 3.50,
#         "soda": 3.00,
#         "lemonade": 4.25}
#
# cart = []
# total = 0
# print("-----------MENU--------------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("-----------------------------")

# while True:
#     food = input("Select an ite (q to quit)").lower()
#     if food == 'q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print(cart)

# print("------------ Your Oder ----------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
#
# print()
# print(f"Total is: ${total:2f}")


# import random
#
# low = 1
# high = 100
#
# options = ("rock", "paper", "scissors")
# cards = ["2","3","4","5","6","7","8","9","10","J", "K", "Q", "A"]

# number = random.randint(low,high)
# number = random.random()
# option = random.choice(options)
# card = random.choice(cards)
# card = random.shuffle(cards)
# # print(option)
#
# print(card)

# Python number guessing game

# import random
#
# lowest_num = 1
# highest_num = 100
#
# answer = random.randint(lowest_num, highest_num)
#
# guesses = 0
# is_running = True
#
#
# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")
#
#
# while is_running:
#     guess = input("Enter your guess: ")
#
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again")
#         elif guess > answer:
#             print("Too high")
#         else:
#             print(f"CORRECT! The correct answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")


import random

options = ("rock", "paper", "scissors")

running =True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors)")

        print(f"Player: {player}")
        print(f"Computer: {computer}")


        if player == computer:
            print("Its a tie")
        elif player == 'rock' and computer == 'scissors':
            print("You Win!")
        elif player == "paper" and computer == 'rock':
            print("You win")
        elif player == 'scissor' and computer == "paper":
            print("You win")
        else:
            print("You lose!")

        if not input("Play again? (Y/N)").lower() == "y":
            running = False

print("Thanks for playing")






















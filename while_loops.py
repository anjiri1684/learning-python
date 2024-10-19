# while loops = execute some code while some condition remain true

name = input("Enter your name")

while name == '':
    print("You did not enter your name")
    name = input("Enter your name")
print(f"Hello {name}")


age = int(input("Enter your age: "))

while age < 0:
    print("Invalid age")
    age = int(input("Enter your age: "))
if age == 0:
    print("Age can't be 0")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")


food = input("Enter your favorite food (q to quit)")

while not food == 'q':
    food = input("Enter your favorite food (q to quit)")
    if len(food) > 3:
        food = input("Enter your favorite food (q to quit)")
    print(f"You like {food}")
print("Bye")

num = int(input("Enter a number between 1 - 10"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10"))

print(f"Your number is {num}")

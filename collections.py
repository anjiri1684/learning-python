# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates Ok
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "banana", "orange", "coconut"]
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits[-1] = "pineapple"

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "avocado")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))
for fruit in fruits:
    print(fruit)

fruits = {"apple", "banana", "orange", "coconut"}
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits = ("apple", "banana", "orange", "coconut")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("apple"))
print(fruits.count("apple"))

for fruit in fruits:
    print(fruit)

print(fruits)

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("------- YOUR CART -----")

for food in foods:
    print(food, end="")

for price in prices:
    total += price
print("-----------------------")
print(f"Your total is: ${total}")


fruits = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'mango', 'pineapple', 'kiwi', 'peach', 'pear']

vegetables = ['carrot', 'broccoli', 'spinach', 'tomato', 'cucumber', 'lettuce', 'bell pepper', 'onion', 'potato']

meat = ['chicken', 'beef', 'pork', 'lamb', 'turkey', 'salmon', 'tuna', 'shrimp', 'duck', 'venison']

groceries = [fruits, vegetables, meat]
print(groceries[0])

num_pad = (
            (1,2,3),
            (4,5,6),
            (7,8,9),
            ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
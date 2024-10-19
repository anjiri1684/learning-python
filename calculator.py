# Simple calculator
operator = input("Choose between + - / * ")

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
    print("Enter a valid mathematical operator")

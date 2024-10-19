# Python weight converter

unit = input("Enter your unit kg or l: ")

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
    print(f"{unit} is an invalid unit")

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

if (unit == 'c' or unit == "C") or (unit == 'f' or unit == 'F'):
    temp = float(input("Enter the temperature: "))
    if unit == 'c':
        result = round((9 * temp) / 5 + 32, 1)
        print(f"The temperature in Fahrenheit is: {result}^F")
    else:
        result = round((temp - 32) * 5 / 9, 1)
        print(f"The temperature in Celsius is: {temp}^C")
else:
    print(f"{unit.upper()} is not a valid unit")

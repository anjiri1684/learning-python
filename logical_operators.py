#
# logical operators = evaluate multiple conditions (or, and , not)
#                     or = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the condition (not False, not True)


temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor is still scheduled")


temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside🥵")
    print("Its sunny ☀️")
elif temp <= 0 and is_sunny:
    print('It is Cold outside 🥶')
    print("Its sunny ☀️")
elif 28 > temp < 0 and is_sunny:
    print('It is warm outside 🥴')
    print("Its sunny ☀️")

print(not is_sunny)

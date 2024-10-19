# for loops = execute a block of code a fixed number of times.
# you can iterate over a range, strings, sequence, etc


for x in reversed(range(1)):
    print(x)

print("HAPPY NEW YEAR")


credit_card = '1234-5678-9012-3456'

for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 3:
        break
    else:
        print(x)


import time

my_time = int(input("Enter the time in seconds"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES UP")


# nested loops = A loop within another loop (outer, inner)
# outer loop
# inner loop

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print("")
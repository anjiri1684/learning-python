# indexing = accessing elements of a sequence using [] (indexing operators)
# [start : end: step ]

credit_number = "1234-5678-9012-3456"
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])
last_digits = credit_number[-5:]
credit_number = credit_number[::-1]
print(credit_number)

# format specifiers = {value: flags} format value based on what flags are inserted

price1 = 30000.14159
price2 = -90087.65
price3 = 1200.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
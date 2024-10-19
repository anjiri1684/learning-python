# function = A blck of resusable code
#            Place () after the function name to invoke it


def birthday_song(name = "Vincent", age = 24):
    print(f"Happy birthday {name}")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()


birthday_song("Anjiri", 25)
birthday_song()
birthday_song()


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Vincent", 50, "01/01")

# return = statement used to end a function
#          and send result back to the caller

def add(x, y):
    z = x + y
    return  z

def subtract(x, y):
    z = x - y
    return  z

def multiply(x, y):
    z = x * y
    return  z

def divide(x, y):
    z = x / y
    return  z

print(divide(1, 2))


def create_full_name(firstname, lastname):
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    return  firstname + " " +lastname

fullname = create_full_name("Vincent", "anjiri")

print(fullname)

# default arguments = A default value for certain parameters
# default is used when that argument is omitted
# make your funtion more flexible reduces number of arguments
# 1. positional, 2. Default, 3. Keyword, 4. arbitrary

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price *( 1 - discount) * (1 + tax)


print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0.16))

import time
def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

print(count(0, 10))



def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Heloo", "Mr", "Vincent", "Anjiri")


for x in range(1, 11):
    print(x, end=" ")
    print()

def get_phone(country_code, area_code, first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"

phone_num = get_phone(country_code=254, area_code=512, first_digits=123, last_digits=123)

print(phone_num)



def add(*args):
    total = 0
    for arg in args:
        total /=arg
    return total

print(add(1, 3, 6, 8))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}, {value}")

print(print_address(street="1234", city="Nairobi", state="NA", zip="05142", apt="100"))

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")

shipping_label("Dr", "Vincent", "Anjiri", "III",
               street= "1233, fake str",
               apt="100",
               city="Nairobi",
               state="Emb",
               zip="00512")


def addition(*args):
    total = 0
    for arg in args:
        total -=arg
    return total
print(addition(3,0,7))

# iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1,2,3,4,5,6]
for num in numbers:
    print(num)

import math

# Math functions
x = 3.14
y = 4
z = 5

# results = round(x)
# results = abs(y)
# results = pow(y, 3)

results = max(x,y,z)
results = min(x,y,z)
print(results)


x = 9 + 0.5
print(math.pi)
print(math.e)
results = math.sqrt(x)
results = math.ceil(x)
print(results)

calPi = math.pi

radius = float(input("Enter the radius "))
circumference = 2 * calPi * radius
circumference = round(circumference, 2)
print(f"The Circumference is {circumference}cm^2")
area_of_circle = calPi * (radius ** 2)
area_of_circle = round(area_of_circle, 3)
print(f"The calculated area of the circle is {area_of_circle}cm^2")

# calculating the area of hypotenuse triangle

length = float(input("Enter the length "))
width = float(input("Enter the width "))
side = math.sqrt(pow(length, 2) + pow(width, 2))
side = round(side, 3)
print(f"The calculated area is {side}cm^2")


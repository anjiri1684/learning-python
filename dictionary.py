
# dictionary = a collection of {key:value}pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "Kenya": "Nairobi"}


print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))


if capitals.get("Kenya"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()
values = capitals.values()
for key in keys:
    print(key)

print()

for value in values:
    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key} ===== {value}")

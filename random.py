import random

low = 1
high = 100

options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","J", "K", "Q", "A"]

number = random.randint(low,high)
number = random.random()
option = random.choice(options)
card = random.choice(cards)
card = random.shuffle(cards)
print(option)

print(card)
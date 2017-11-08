import random

lines = open("QuoteoftheDay.txt").read().splitlines()
quote =random.choice(lines)
print(quote)
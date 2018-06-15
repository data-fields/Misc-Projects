import random

#Opens a quote filled text file and reads it line by line
lines = open( "QuoteoftheDay.txt" ).read().splitlines()

#Randomly chooses a line from the text file
quote = random.choice( lines )

#Prints the randomly chosen line
print(quote)
 

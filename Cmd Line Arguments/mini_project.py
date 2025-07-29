# Mini Project - Happiness Calculator
import sys

# Get the three strings from command line
string1 = sys.argv[1]  # Numbers you like
string2 = sys.argv[2]  # Numbers you dislike  
string3 = sys.argv[3]  # Numbers given to you

# Split strings to get numbers
liked_numbers = string1.split('-')
disliked_numbers = string2.split('-')
given_numbers = string3.split('-')

# Calculate happiness
happiness = 0

for number in given_numbers:
    if number in liked_numbers:
        happiness = happiness + 1
    elif number in disliked_numbers:
        happiness = happiness - 1

print(happiness)

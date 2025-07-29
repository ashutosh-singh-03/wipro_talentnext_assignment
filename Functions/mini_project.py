# Function to sort colors alphabetically
def sort_colors(color_string):
    # Split the colors by hyphen
    colors = color_string.split('-')
    print(f"Original colors: {colors}")
    
    # Sort the colors alphabetically
    colors.sort()
    print(f"Sorted colors: {colors}")
    
    # Join them back with hyphens
    sorted_string = '-'.join(colors)
    return sorted_string

# Project 1 - Color Sorting Function
print("Project 1 - Color Sorting Function")
user_input = input("Enter colors separated by hyphens: ")
user_result = sort_colors(user_input)
print(f"Your sorted result: {user_result}")


# Project 2 - Using String Utility Module
import strings_util
name = input("Enter a name: ")
print(f"Input: {name}")

# Use all three functions from the module
palindrome_result = strings_util.ispalindrome(name)
vowel_count = strings_util.count_vowels(name)
letter_freq = strings_util.letter_frequency(name)

print(palindrome_result)
print(f"No of vowels: {vowel_count}")
print(f"Frequency of letters: {letter_freq}")

# Program 1
# Write a program to count the number of upper and lower case letters in a String.

sample_string = "Hello World Python"
print(f"Original String: {sample_string}")

upper_count = 0
lower_count = 0

for char in sample_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")


# Program 2
# Write a program that will check whether a given String is Palindrome or not.

test_string = input("Enter a string to check palindrome: ")
print(f"Original String: {test_string}")

test_string = test_string.lower()

if test_string == test_string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# Program 3
# Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.

input_string = "Wipro"
print(f"Input String: {input_string}")

first_two = input_string[:2]
print(f"First 2 characters: {first_two}")

string_length = len(input_string)
print(f"Length of string: {string_length}")

result = first_two * string_length
print(f"Output: {result}")


# Program 4
# Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged.

test_string_2 = "xHix"
print(f"Input String: {test_string_2}")

result_string = test_string_2

if len(result_string) > 0 and result_string[0] == 'x':
    result_string = result_string[1:]

if len(result_string) > 0 and result_string[-1] == 'x':
    result_string = result_string[:-1]

print(f"Output: {result_string}")


# Program 5
# Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.

input_string_2 = "Wipro"
n = 3
print(f"Input String: {input_string_2}")
print(f"Value of n: {n}")

last_n_chars = input_string_2[-n:]
print(f"Last {n} characters: {last_n_chars}")

final_result = last_n_chars * n
print(f"Output: {final_result}")

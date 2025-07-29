# Program 1
# Write a program to add a key and value to a dictionary.

sample_dict = {0: 10, 1: 20}
print(f"Original Dictionary: {sample_dict}")

# Add new key-value pair
sample_dict[2] = 30
print(f"After adding key 2 with value 30: {sample_dict}")


# Program 2
# Write a program to concatenate the following dictionaries to create a new one.

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Dictionary 3: {dict3}")

# Concatenate dictionaries
new_dict = {}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print(f"Concatenated Dictionary: {new_dict}")


# Program 3
# Write a program to check if a given key already exists in a dictionary.

test_dict = {1: 10, 2: 20, 3: 30, 4: 40}
print(f"Test Dictionary: {test_dict}")

key_to_check = int(input("Enter key to check: "))

if key_to_check in test_dict:
    print(f"Key {key_to_check} exists in the dictionary")
else:
    print(f"Key {key_to_check} does not exist in the dictionary")


# Program 4
# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

sample_dict_4 = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
print(f"Dictionary: {sample_dict_4}")

# Print keys alone
print("Keys alone:")
for key in sample_dict_4:
    print(key, end=" ")

# Print values alone
print("\nValues alone:")
for key in sample_dict_4:
    print(sample_dict_4[key], end=" ")

# Print both keys and values
print("\nBoth keys and values:")
for key in sample_dict_4:
    print(f"{key}: {sample_dict_4[key]}")


# Program 5
# Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.

squares_dict = {}

# Create dictionary with keys 1-15 and values as squares
for i in range(1, 16):
    squares_dict[i] = i * i

print("Dictionary with keys 1-15 and their squares:")
print(squares_dict)


# Program 6
# Write a program to sum all the values in a dictionary, considering the values will be of int type.

int_dict = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
print(f"Dictionary: {int_dict}")

total = 0
for key in int_dict:
    total = total + int_dict[key]

print(f"Sum of all values: {total}")

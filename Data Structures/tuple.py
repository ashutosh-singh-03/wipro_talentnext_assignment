# Program 1
# Write a program to print the 4th element from first and 4th element from last in a tuple.

sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original Tuple: {sample_tuple}")

# 4th element from first
four_first = sample_tuple[3]
print(f"4th element from first: {four_first}")

# 4th element from last
four_last = sample_tuple[-4]
print(f"4th element from last: {four_last}")


# Program 2
# Write a program to check whether an element exists in a tuple or not.

print(f"Original Tuple: {sample_tuple}")

element = int(input("Enter element to check: "))

if element in sample_tuple:
    print(f"Element {element} exists in the tuple")
else:
    print(f"Element {element} does not exist in the tuple")


# Program 3
# Write a program to convert a list into a tuple.

sample_list = [1, 2, 3, 4, 5]
print(f"Original List: {sample_list}")

# Convert list to tuple
converted_tuple = tuple(sample_list)
print(f"Converted Tuple: {converted_tuple}")


# Program 4
# Write a program to find the index of an item in a tuple.

print(f"Tuple: {sample_tuple}")

item = input("Enter item to find index: ")

if item in sample_tuple:
    index = sample_tuple.index(item)
    print(f"Index of '{item}': {index}")
else:
    print(f"'{item}' not found in tuple")


# Program 5
# Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f"Original List of Tuples: {tuple_list}")

# Replace last value of each tuple with 100
new_tuple_list = []
for t in tuple_list:
    temp_list = list(t)
    temp_list[-1] = 100
    new_tuple = tuple(temp_list)
    new_tuple_list.append(new_tuple)

print(f"After replacing last values with 100: {new_tuple_list}")

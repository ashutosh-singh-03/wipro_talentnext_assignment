# Program 1
# Write a program to remove a given item from the set.

sample_set = {10, 20, 30, 40, 50}
print(f"Original Set: {sample_set}")

item_to_remove = int(input("Enter item to remove: "))

if item_to_remove in sample_set:
    sample_set.remove(item_to_remove)
    print(f"After removing {item_to_remove}: {sample_set}")
else:
    print(f"Item {item_to_remove} not found in set")


# Program 2
# Write a program to create an intersection of sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

intersection_set = set1.intersection(set2)
print(f"Intersection of sets: {intersection_set}")


# Program 3
# Write a program to create an union of sets.

set3 = {10, 20, 30}
set4 = {30, 40, 50}
print(f"Set 3: {set3}")
print(f"Set 4: {set4}")

union_set = set3.union(set4)
print(f"Union of sets: {union_set}")


# Program 4
# Write a program to find the maximum and minimum value in a set.

number_set = {45, 12, 78, 23, 67, 89, 34}
print(f"Number Set: {number_set}")

max_value = max(number_set)
print(f"Maximum value: {max_value}")

min_value = min(number_set)
print(f"Minimum value: {min_value}")

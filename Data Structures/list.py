# Program 1
# Write a program to create a list of 5 integers and display the list items.
# Access individual elements through index.

int_list = [1,2,34,4,5]
# print directly
print(int_list)

# print via index
for item in int_list:
    print(item, end=" ")


# Program 2
# Write a program to append a new item to the end of the list.
int_list.append(75)
int_list.append(75)
print(f"\nUpdated List: {int_list}")


# Program 3
# Write a program to reverse the order of the items in the list.
int_list.reverse()
print(f"Reversed List: {int_list}")

# Program 4
# Number of occurrences of an element
target = int(input("Enter the element: "))
count = 0

for item in int_list:
    if item == target:
        count += 1

print(f"Total Occurrences of {target}: {count}")


# Program 5
# Write a program to append the items of list1 to list2 in the front.
list1 = [10, 20, 30]
list2 = [40, 50, 60]
print(f"Original list1: {list1}")
print(f"Original list2: {list2}")


for item in reversed(list1):
    list2.insert(0, item)

print(f"After appending list1 to front of list2: {list2}")

# Program 6
# Adding new item before second element
print(f"Original List: {int_list}")
ele = int(input("Enter the element: "))
int_list.insert(1, ele)
print(f"After Addition: {int_list}")

# Program 7
# Remove any element from a specified index
print(f"Original List: {int_list}")
index = int(input("Enter the index: "))

if index < len(int_list) and index >= 0:
    removed_element = int_list.pop(index)
    print(f"Removed element: {removed_element}")
else:
    print("Invalid index")
    
print(f"After Removal: {int_list}")


# Program 8
# Remove first occurrence of an element
print(f"Original List: {int_list}")
element = int(input("Enter the element: "))

if element not in int_list:
    print("Element not found")
else:
    int_list.remove(75)
    
print(f"After Removal: {int_list}")
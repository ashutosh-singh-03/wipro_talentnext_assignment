# Project 1 - Dictionary
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Initial list of people and facts:")
for person in people_facts:
    print(person + ": " + people_facts[person])

# Change
people_facts["Jeff"] = "Is afraid of heights."

# Add
people_facts["Jill"] = "Can hula dance."

# Display the updated list
print("\nAfter changes:")
for person in people_facts:
    print(person + ": " + people_facts[person])


# Project 2 - List
# Find the runner-up score from a list of scores
scores = [2, 3, 6, 6, 5]
print("\nOriginal scores list:", scores)

# Remove duplicates
unique_scores = list(set(scores))
print("Unique scores:", unique_scores)

# Sort
unique_scores.sort()
print("Sorted unique scores:", unique_scores)

# Get the second highest score
runner_up = unique_scores[-2]
print("Runner-up score:", runner_up)


# Project 3 - List and Dictionary
# Student records with average marks calculation
student_records = {
    "Ashutosh": [67, 68, 69],
    "Shivam": [70, 98, 63],
    "Pinkesh": [52, 56, 60]
}

student_name = input("\nEnter a name: ")

# Check if student exists
if student_name in student_records:
    marks = student_records[student_name]
    print("Marks for " + student_name + ": " + str(marks))
    
    # Calculate average
    total_marks = 0
    for mark in marks:
        total_marks = total_marks + mark
    
    average = total_marks / len(marks)
    print("Average percentage mark: " + str(int(average)))
else:
    print("Student not found in records")


# Project 4 - Strings
# Count how many times Alex's name appears in a string
input_String = input("Enter the String: ")
print("\nOriginal String: " + input_String)

name_to_find = input("Enter the Name: ")
print("Name to find: " + name_to_find)

# Count occurrences of the name
count = 0
words = input_String.split()

for word in words:
    if name_to_find in word:
        count = count + 1

print("Number of times " + name_to_find + " appears: " + str(count))
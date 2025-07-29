# Program 1  
# Write a program to read the entire content from a txt file and display it to the user.

file = open("sample.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()


# Program 2
# Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter number of lines to read: "))
file = open("sample.txt", "r")
lines = file.readlines()

print(f"First {n} lines:")
for i in range(n):
    if i < len(lines):
        print(lines[i], end="")

file.close()


# Program 3
# Write a program to accept input from user and append it to a txt file.

user_input = input("Enter text to append: ")
file = open("sample.txt", "a")
file.write(user_input + "\n")
file.close()
print("Text appended to file")


# Program 4
# Write a program to read contents from a txt file line by line and store each line into a list.

file = open("sample.txt", "r")
lines_list = []
for line in file:
    lines_list.append(line.strip())

file.close()
print("Lines stored in list:")
print(lines_list)


# Program 5
# Write a program to find the longest word from the txt file contents.

file = open("sample.txt", "r")
content = file.read()
file.close()

words = content.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)


# Program 6
# Write a program to count the frequency of a user entered word in a txt file.

search_word = input("Enter word to search: ")
file = open("sample.txt", "r")
content = file.read()
file.close()

words = content.split()
count = 0

for word in words:
    if word.lower() == search_word.lower():
        count = count + 1

print(f"Frequency of '{search_word}':", count)

# Mini Project - Secret Message Decoder

file = open("sample2.txt", "r")
lines = file.readlines()
file.close()

num_lines = len(lines)
print("Number of lines:", num_lines)

if num_lines <= 12:
    meeting_time = str(num_lines) + " AM"
else:
    hour = num_lines - 12
    meeting_time = str(hour) + " PM"

print("Meeting time:", meeting_time)

file = open("sample2.txt", "r")
content = file.read()
file.close()

words = content.lower().split()

word_count = {}
for word in words:
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word = clean_word + char
    
    if clean_word != "":
        if clean_word in word_count:
            word_count[clean_word] = word_count[clean_word] + 1
        else:
            word_count[clean_word] = 1

max_count = 0
most_frequent_word = ""

for word in word_count:
    if word_count[word] > max_count:
        max_count = word_count[word]
        most_frequent_word = word

meeting_place = most_frequent_word.capitalize() + " Street"
print("Meeting place:", meeting_place)

# Program 1: Create a dictionary with odd numbers from the input list as keys and values
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_dict = {x: x for x in input_list if x % 2 != 0}
print("Dictionary with odd numbers:", odd_dict)

# Program 2: Map each English alphabet to its corresponding integer
alphabet_dict = {chr(96 + i): i for i in range(1, 27)}
print("Alphabet mapping (letter: number:", alphabet_dict)
# Program 1 - Write a function to return the sum of all numbers in a list.
list_input = [1,2,3,4,5,5]

def sum_list(list_int):
    sum = 0
    for item in list_int:
        sum += item
    
    print(f"Sum: {sum}")

sum_list(list_input)

# Program 2 - Write a function to reverse a string
inp_string = input("Enter a string: ")

def rev_string(s):
    rev = s[::-1]
    print(rev)

rev_string(inp_string)

# Program 3 - Function to return the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        print(f"Factorial is 1.")
    else:
        prod = 1 
        for i in range(1, num + 1):
            prod *= i
        print(f"Factorial of {num} is {prod}.")

num = int(input("Enter a number: "))
factorial(num)


# Program 4 - Function to return the number of upper and lower cases from a string
def upper_lower_count(inp):
    upper_count = 0
    lower_count = 0

    for char in inp:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")

upper_lower_count(inp_string)


# Program 5 - function to return the even numbers from a list
def even(list_input):
    even_list = []
    for item in list_input:
        if item % 2 == 0:
            even_list.append(item)
    
    print(f"List with even elements are: {even_list}")
    
sample_list = [1,2,3,4,5,6,7,8]
even(sample_list)

# Program 6 - function to check prime number
def prime(num):
    if num < 2:
        print(f"{num} is not Prime.")
        return
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not Prime.")
            return
    
    print(f"{num} is Prime.")
        
num = int(input("Enter a number: "))
prime(num)
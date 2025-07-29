# Program 1
# Write a program to accept two numbers from the user and perform division.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter valid numbers")


# Program 2  
# Write a program to accept a number from the user and check whether it's prime or not.

try:
    num = int(input("Enter a number: "))
    
    if num < 2:
        print("Not a prime number")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")
            
except ValueError:
    print("Error: Please enter a valid number")


# Program 3
# Write a program to accept the file name to be opened from the user.

try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    content = file.read()
    print("File content in title case:")
    print(content.title())
    file.close()
except FileNotFoundError:
    print("Error: File not found")


# Program 4
# Declare a list with 10 integers and ask the user to enter an index.

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print("List:", numbers)

try:
    index = int(input("Enter an index (0-9): "))
    number = numbers[index]
    
    if number > 0:
        print("Number at index", index, "is positive:", number)
    elif number < 0:
        print("Number at index", index, "is negative:", number)
    else:
        print("Number at index", index, "is zero:", number)
        
except IndexError:
    print("Error: Invalid index. Please enter index between 0-9")
except ValueError:
    print("Error: Please enter a valid index number")

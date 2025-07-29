# Program 1
# Write a program to accept two numbers as command line arguments and display their sum.
import sys

print("Arguments provided:", sys.argv)

if len(sys.argv) == 3:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    sum_result = num1 + num2
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Sum:", sum_result)
else:
    print("Please provide exactly 2 numbers")


# Program 2
# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
filename = sys.argv[0]
print("File name:", filename)

if len(sys.argv) > 1:
    welcome_message = ""
    for i in range(1, len(sys.argv)):
        welcome_message = welcome_message + sys.argv[i] + " "
    print("Welcome message:", welcome_message)
else:
    print("No welcome message provided")


# Program 3
# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if len(sys.argv) > 1:
    numbers = []
    for i in range(1, len(sys.argv)):
        numbers.append(int(sys.argv[i]))
    
    print("Numbers provided:", numbers)
    
    prime_numbers = []
    prime_sum = 0
    
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
            prime_sum = prime_sum + num
    
    print("Prime numbers:", prime_numbers)
    print("Sum of prime numbers:", prime_sum)
else:
    print("No numbers provided")

# Program 1: Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
print()

# Program 2: Check if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print()

# Program 3: Check if two numbers have the same last digit
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)
print()

# Program 4: Print numbers from 1 to 10 in a single row with tab space
for i in range(1, 11):
    print(i, end="\t")
print()
print()

# Program 5: Print even numbers between 23 and 57, each in separate row
for i in range(24, 58, 2):
    print(i)
print()

# Program 6: Check if a number is prime or not
num = int(input("Enter a number: "))
if num < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
print()

# Program 7: Print prime numbers between 10 and 99
for num in range(10, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
print()

# Program 8: Sum of all digits of a given number
num = int(input("Enter a number: "))
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(digit_sum)
print()

# Program 9: Reverse a given number
num = int(input("Enter a number: "))
reversed_num = 0
temp = num
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
print(reversed_num)
print()

# Program 10: Check if a number is palindrome
num = int(input("Enter a number: "))
reversed_num = 0
temp = num
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10

if num == reversed_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

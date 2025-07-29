# Module: strings_util.py
# Functions for string operations

def ispalindrome(name):
    """Check if the given name is a palindrome"""
    # Remove spaces and convert to lowercase for comparison
    clean_name = name.replace(" ", "").lower()
    
    # Check if string is same when reversed
    if clean_name == clean_name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_vowels(name):
    """Count the number of vowels in the given name"""
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in name:
        if char in vowels:
            count = count + 1
    
    return count

def letter_frequency(name):
    """Count how many times each letter appears in the name"""
    frequency = {}
    
    # Count each character (excluding spaces)
    for char in name:
        if char != " ":
            char = char.lower()  # Convert to lowercase for consistency
            if char in frequency:
                frequency[char] = frequency[char] + 1
            else:
                frequency[char] = 1
    
    # Create result string
    result_parts = []
    for letter in sorted(frequency.keys()):
        result_parts.append(f"{letter}-{frequency[letter]}")
    
    return ", ".join(result_parts)

'''
Matthew Kilpatrick
Chapter 12 Recursion
'''
from tabulate import tabulate
import random
import pygame
import numpy
import pandas
from collections import deque
def main():
    number = 0
    number = int(input("How many numbers to display?: "))
    print_num(number)
def print_num(n):
    if n > 1:
        print_num(n-1)
    print(n, sep=" ")
#main()
# That example was stupid here is a better example of a recurive function:
def main2():
    message()
def message():
    print("This is a recursive function.")
    message()
print()
def recursive():
    message(5)
def message(times):
    if times > 0:
        print("This is an example of recursive function!!!")
        message(times-1)
recursive()
print()
#main2()
# A recursive function executes slower than its iterative counterpart on the traditional Von-Neumann computers
# Which type of algorithm runs faster?
# A recursive function executes slower than its iterative counterpart
# Also a recursive function calls takes a lot of memory space
# Exercise 3.4.1 (Remove Odd Digits - String)
'''
Write a function removeOddDigits(inString) that takes a single String parameter. 
inString, and returns a new String containing only the even-digits from the initial inString.
The function should return an empty string if there are no even digits.
'''


def removeOddDigits2(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0

    # Extract the last digit
    last_digit = n % 10

    # Recursively call removeOddDigits on the remaining digits
    result = removeOddDigits2(n // 10)

    # Check if the last digit is even
    if last_digit % 2 == 0:
        # If even, append it to the result
        return result * 10 + last_digit
    else:
        # If odd, return only the result without appending the odd digit
        return result


# Test the function
print(removeOddDigits2(123456789))  # Output: 2468
print(removeOddDigits2(13579))  # Output: 0

def removeOddDigits(inString):
    if inString == "":
        return ""

    # Check if the first character is a digit and even
    if inString[0].isdigit() and int(inString[0]) % 2 == 0:
        # If even, append to the result and recurse on the rest of the string
        return inString[0] + removeOddDigits(inString[1:])
    else:
        # If odd, simply recurse on the rest of the string
        return removeOddDigits(inString[1:])

# Do not change the code below, it's for testing purpose
print(removeOddDigits(input("Enter String:")))

print("Doing the same thing but with a loop: ")
def removeOddDigits(inString):
    even_digits = ""
    for char in inString:
        if char.isdigit() and int(char) % 2 == 0:
            even_digits += char
    return even_digits

# Test the function
print(removeOddDigits("Hello12345World"))  # Output: 24
print(removeOddDigits("ThisStringHasNoEvenDigits"))  # Output: ""
'''
Repeat Digit one more time…
Write a function repeat_digits(n), which takes a positive integer n and returns another integer that is identical to n 
but with each digit repeated one more time.
'''
def repeat_digits(n):
    # Base case: if n is a single digit, return n repeated twice
    if n < 10:
        return n * 11

    # Recursive case: repeat digits of n except for the last digit
    # and append the last digit twice
    return repeat_digits(n // 10) * 100 + ((n % 10) * 11)

# Example usage:
number = 1234
result = repeat_digits(number)
print("Original Number:", number)
print("Number with each digit repeated one more time:", result)
print()
'''
Are Digits Sequence Increasing (Non-Decreasing digits)?
Write a function is_increasiong(n) that takes a parameter n and returns True when if the sequence of digits is an increasing (non-decreasiong) order, False otherwise.
Single digits are by default to be True.
'''


def is_increasing(n):
    # Base case: single digit number is always considered increasing
    if n < 10:
        return True

    # Recursive case: check if the last two digits are in increasing order,
    # and recursively check the rest of the digits
    last_digit = n % 10
    second_last_digit = (n // 10) % 10

    if last_digit < second_last_digit:
        return False

    return is_increasing(n // 10)

# Example usage:
number = 1234
print("Original Number:", number)
print("Is the sequence of digits increasing?", is_increasing(number))

number = 54321
print("\nOriginal Number:", number)
print("Is the sequence of digits increasing?", is_increasing(number))
'''
'''


'''
Matthew Kilpatrick
4/21/24
'''
import pandas
import numpy
import random
from collections import deque
from tabulate import tabulate
import pygame
import CodioLabRecursion
import turtle

factorial = CodioLabRecursion.Recursion()
def example1():
    print("\nExample 1: Intro Using Factorial ")
    number = int(input("Enter a number you want to find the factorial of: ")) # Getting a number from user
    print(f"The factorial of {number}! = {factorial.factorial_recursively(number)}") # calling the factorial functional
def example2():
    print("\nExample 2: Base Case Work")
    number = int(input("Enter a number you want to find the factorial of: ")) # Getting a number from user
    print(f"The factorial of {number}! = {factorial.factorial_recursively_with_NO_BASE(number)}") # calling the factorial functional
def example3():
    print("\nExample 3: Fibonacci Sequence")
    print(f"The Fibonnaci Number of {6} - {factorial.Fibonacci_Number(6)}") #   # Output: 8 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8)
    print(f"The Fibonnaci Number of {8} - {factorial.Fibonacci_Number(8)}")
def example4():
    print(f"\nExample 4: Adding The Predetermined Length:  ")
    length = 10
    print(f"The Length Of The Sequence: {length}")
    for num in range(length):
        print(factorial.Fibonacci_Sequence(num), end= ", ")
def example5():
    print(f"\nExample 5: Fibonacci Sequence Data Structure: ")
    length = 90
    for num in range(length):
        print(num, end= ", ")
def example6(): # For example, find_sum(5) would add up the numbers 0 to 5. Note, you must use a docstring, and not all of the blocks will be used.
    print(f"\nExample 6: Finding The Sum Of Number Up To N: ")
    print(f"The Sum Of Numbers From 0 to {10}: {factorial.Sum_Of_Numbers_Up_To_N_Recursion(10)}")

# example2()
# example3()
# example4()

#example6()

def example7():
    print("\nRecursive Power")
    print(factorial.recursive_power(5, 3))  # Output: 125
    print(factorial.recursive_power(4, 5))  # Output: 1024
example7()
def example8():
    print("\nRecursive Sum")
    print(factorial.recursive_sum(5))  # Output: 15
    print(factorial.recursive_sum(10))  # Output: 55
example8()
def example9():
    print("\nList Sum Recursion: ")
    print(factorial.list_sum([1, 2, 3, 4, 5]))  # Output: 15
    print(factorial.list_sum([10, 12.5, 10, 7]))  # Output: 39.5
example9()
def example10():
    print("\nBunny Ears")
    print(factorial.bunny_ears(8))  # Output: 16
    print(factorial.bunny_ears(0))  # Output: 0
example10()
def example11():
    print("\nReverse String")
    print(factorial.reverse_string("cat"))  # Output: 16
    print(factorial.reverse_string("mouse"))  # Output: 0
example11()
def example12():
    print("\nGetting The Max")
    print(factorial.get_max([1, 2, 3, 4, 5]))  # Output: 5
    print(factorial.get_max([11, 22, 3, 41, 15]))  # Output: 41
    print("\nGetting The Min: ")
    my_list = [5, 3, 9, 1, 7]
    list = []
    for num in range(20):
        num = random.randint(2,67)
        list.append(num)

    print(factorial.find_smallest(my_list))
    print(f"Second List: {list} ")
    print(factorial.find_smallest(list))
    print("\nSearch A List Using Recursion: ")
    list2 = []
    for nums in range(21): # Up to 21 to include the number 20 but not include 21
        nums = random.randint(1,50)
        list2.append(nums)
    print(f"The List We Are Going To Search: \n\t{list2}")
    target = random.choice(list2)
    print(f"Search Value = {target}")
    index = factorial.Search_List_RecursionStyleYemme(list2,searchValue=target)
    if index != -1:
        print(f"The Search Value {target} was found at {index}")

    else:
        print(f"The Search Value {target} was not found!")

    print("Total sum of names with 'm' in the 4th position: ")
    names = ['Sam', 'Tom', 'Michael', 'Emma', 'Mason']
    total_sum = factorial.sum_names_with_m(names)
    print(f"Total sum of names with 'm' in the 4th position: {total_sum}")
    print("Reversing A List: ")
    print(f"Reverse Of {names} - {factorial.reverse_list(names)}")


example12()
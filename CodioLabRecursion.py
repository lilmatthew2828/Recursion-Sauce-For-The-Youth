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

# Recursion:
#   What is Recursion :
#      - Solving a coding problem with functions involves breaking down the problem into smaller problems.
#      - When these smaller problems are variations of the larger problem (also know as self-similar), then RECURSION can be used.
# Example 1 of Recursion: The mathematical function "factorial" is self-similar
#       Five factorial (5!) = 5 * 4 * 3 * 2 * 1
# Because Five Factorial is self-similar, recursion can be used !!!!
class Recursion:
    def __init__(self):
        self.fibcache = {} # for the fibonacci sequence effiency/Datastructure example
    def factorial_recursively(self, n): # When N is 5, python starts a multiplication problem of 5 * factorial(4)
        if(n == 1): # Then the function runs again and the multiplication problem is now 5 * factorial(3)
            return 1 # Then the function runs again and the multiplication problem is now 5 * factorial(2)
        else: # Then the function runs again and the multiplication problem is now 5 * factorial(1)
            return n * self.factorial_recursively(n - 1) # This continues until n is 1. Python returns the value 1, and Python solves the multiplication problem 5 * 4 * 3 * 2 * 1.


    # print("\nExample 1: Intro Using Factorial ")
    # number = int(input("Enter a number you want to find the factorial of: ")) # Getting a number from user
    # print(f"The factorial of {number}! = {factorial_recursively(number)}") # calling the factorial functional
    '''
    More About Recursive Functions:
        - Recursive Functions are functions that call themselves
    The Base Case:
        - Each recursive function has two part: 
            1. The Recursive Case = This is where the function calls its self with a different parameter.
            
            2. The Base Case = This is where the function stops calling itself and returns a value.
                - The base case is the most important part of a recursive function.
                - Without it, the function will never stop calling itself. 
                    - Like an infinite loop, Python will stop the program with an error.
    '''
    def factorial_recursively_with_NO_BASE(self, n): # When N is 5, python starts a multiplication problem of 5 * factorial(4)
        '''No Base Case !!!!!!!!'''
        # Then the function runs again and the multiplication problem is now 5 * factorial(1)
        return n * self.factorial_recursively(n - 1) # This continues until n is 1. Python returns the value 1, and Python solves the multiplication problem 5 * 4 * 3 * 2 * 1.
    #
    # print("\nExample 2: Base Case Work")
    # number = int(input("Enter a number you want to find the factorial of: ")) # Getting a number from user
    # print(f"The factorial of {number}! = {factorial_recursively(number)}") # calling the factorial functional


    # Fibonacci Sequence:
    # Fibonacci Number:
    # A Fibonacci number is a number in which the current number is the sum of the previous two Fibonacci numbers.
    '''
    Calculating a Fibonacci number is self-similar, which means it can be defined with recursion.
    Setting the base case is important to avoid infinite recursion.
    When the number n is 0 the Fibonacci number is 0, and when n is 1 the Fibonacci number is 1.
    So if n is less than or equal to 1, then return n. That is the base case.
    '''
    def Fibonacci_Number(self, n): # Recursive case: F(n) = F(n-1) + F(n-2)
        if( n <= 1): # When n is 0 or 1 the Fibonacci number is 0 or 1
            return n
        else: # When the number is not 0 or 1
            return(self.Fibonacci_Number(n - 1) + self.Fibonacci_Number(n - 2)) # This means we compute the sum of the (n-1)th and (n-2)th Fibonacci numbers

    def Fibonacci_Sequence(self,n):
        if(n <= 1):  # When n is 0 or 1 the Fibonacci number is 0 or 1
            return n
        else: #
            return(self.Fibonacci_Sequence(n-1) + self.Fibonacci_Sequence(n-2))
    '''
    Why is Python timing out? 
    The code written above is terribly inefficient. 
    Each time through the loop, Python is calculating the same Fibonacci numbers again and again.
    When num is 1, Python calculates the Fibonacci numbers for 0 and 1. 
    When num is 2, Python is calculating the Fibonacci numbers for 0, 1, and 2. 
    Once num becomes large enough, it becomes too much work for Python to have to recalculate these large numbers over and over again. 
    There is a more efficient way to do this by using a data structure called a dictionary. 
    The idea is to store previously calculated Fibonacci numbers in the dictionary. 
    So instead of recalculating the same numbers again and again, you can get these numbers from the dictionary. 
    If a Fibonacci number is not in the dictionary, then calculate it and add it to the dictionary. 
    Data structures are a bit beyond the scope of these lessons, but here is the code of a more efficient way to calculate and print the Fibonacci sequence. Copy and paste the code below into the IDE if you want to run it.
    '''
    def Fibonacci_DataStructure(self, n):
        # Check To see if a fibonacci number has been calculated in the dictionary
        # If not, add it to the dictionary and return it
        # if yes, return the number from the dictionary
        if n not in self.fibcache.keys():
            self.fibcache[n] = self.Fibonacci_num(n)
        return self.fibcache[n]
    def Fibonacci_num(self,n):
        if n <= 1:
            return n
        else:
            fib = self.Fibonacci_DataStructure((n-1) + self.Fibonacci_DataStructure(n-2))
            return fib

    def Sum_Of_Numbers_Up_To_N_Recursion(self, n):
        if n == 0:
            return 0
        else:
            return (n + self.Sum_Of_Numbers_Up_To_N_Recursion(n - 1))

    '''
     Write a recursive function called recursive_power that takes two integers as parameters. 
     The first parameter is the base and the second parameter is the exponent. 
     Return the base parameter to the power of the exponent.
     '''

    def recursive_power(self,base, exponent):
        # Base case: exponent is 0, return 1
        if exponent == 0:
            return 1
        # Recursive case: multiply base by recursive call with decremented exponent
        else:
            return base * self.recursive_power(base, exponent - 1)

    '''
    Problem
    Write a recursive function called list_sum that takes a list of numbers as a parameter. 
    Return the sum of all of the numbers in the list. 
    Hint, the slice operator will be helpful in solving this problem.
    '''
    def list_sum(self, lst):
        # Base case: if the list is empty, return 0
        if len(lst) == 0:
            return 0
        # Recursive case: return the first element plus list_sum of the rest of the list
        else:
            return lst[0] + self.list_sum(lst[1:])

    '''
    Problem
    Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter.
    Return the number of bunny ears (2 per bunny). 
    Do not use multiplication; instead use addition.
    '''
    def bunny_ears(self, bunnies):
        # Base case: if there are no bunnies, return 0
        if bunnies == 0:
            return 0
        # Recursive case: return 2 (ears per bunny) plus bunny_ears for one less bunny
        else:
            return 2 + self.bunny_ears(bunnies - 1)
    '''
    Problem
    Write a recursive function called reverse_string that takes a string as a parameter. Return the string in reverse order. Hint, the slice operator will be helpful when solving this problem.
    Expected Output:
        If the function call is reverse_string("cat"), then the function would return tac
        If the function call is reverse_string("house"), then the function would return esuoh
    '''
    def reverse_string(self, string):
        # Base case: if the string is empty or has only one character, return the string itself
        if len(string) <= 1:
            return string
        # Recursive case: return the last character of the string concatenated with the reversed substring
        else:
            return string[-1] + self.reverse_string(string[:-1])

    def reverse_list(self,list):
        if len(list) <= 1:
            return list
        else:
            return list[-1:] + self.reverse_list(list[:-1])

    def sumAListUsingRecursion

    '''
    Problem: Get Max Numbers/ Largest Numbers 
        Write a recursive function called get_max that takes a list of numbers as a parameter. Return the largest number in the list.
        Expected Output:
            If the function call is get_max([1, 2, 3, 4, 5]), then the function would return 5
            If the function call is get_max([11, 22, 3, 41, 15]), then the function would return 41
    '''
    def get_max(self, lst):
        # Base case: if the list has only one element, return that element
        if len(lst) == 1:
            return lst[0]
        else:
            # Recursive case: compare the first element with the maximum of the rest of the list
            return max(lst[0], self.get_max(lst[1:]))

    def find_smallest(self, arr):
        # Base case: if the list has only one element, return that element
        if len(arr) == 1:
            return arr[0]
        # Recursive case: compare the first element with the smallest element of the rest of the list
        else:
            return min(arr[0], self.find_smallest(arr[1:]))

    def Search_List_RecursionStyleYemme(self,list,searchValue,index=0):
        # Base case: if index goes beyond the length of the list, return -1 (indicating not found)
        if(index >= len(list)):
            return -1
        #     # Base case: if the element at the current index matches the target, return the index
        if(list[index] == searchValue):
            return index
        #     # Recursive case: call the function again with incremented index
        return self.Search_List_RecursionStyleYemme(list, searchValue, index + 1)


    # Sure, here's a recursive function in Python that sums all the names in a list where the name has 'm' in the 4th position:
    def sum_names_with_m(self,names, index=0):
        # Base case: if index goes beyond the length of the list, return 0 (indicating sum is 0)
        if index >= len(names):
            return 0

        # Check if the name at the current index has 'm' in the 4th position
        if len(names[index]) >= 4 and names[index][3] == 'm':
            # If 'm' is in the 4th position, add the length of the name to the sum
            return len(names[index]) + self.sum_names_with_m(names, index + 1)

        # If 'm' is not in the 4th position, move to the next name
        return self.sum_names_with_m(names, index + 1)



    '''
    Trees can be drawn recursively. 
    Draw a branch. At the end of the branch, draw two smaller branches with one to the left and the other to the right.
    Repeat until a certain condition is true. 
    This program will walk you through drawing a tree in this way.
    '''
    '''
    The Base Case For Drawing a tree:
        - The base case for this function is a bit different. 
        - In previous examples, if the base case is true a value was returned. 
        - The function recursive_tree does not return a value, it draws on the screen. 
        - So the base case will be to keep recursing as long as branch_length is greater than some value.
    '''

    # turtle.mainloop()
    # Write a recursive function called recursive_sum that takes an integer as a parameter. Return the sum of all integers between 0 and the number passed to recursive_sum.
    def recursive_sum(self, n):
        # Base case: if n is 0, return 0
        if n == 0:
            return 0
        # Recursive case: return n plus recursive_sum with decremented n
        else:
            return n + self.recursive_sum(n - 1)


    # Test cases













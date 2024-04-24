'''
Matthew Kilpatrick
Learning Recursion From A Youtube Video
4/11/24
'''
import random
import pandas
import numpy
import pygame
from tabulate import tabulate

# Recursion - A function that calls itself from within,
# helps to visualize a complex problem into basic steps, which can be solved more easily iteratively
# Recursion is defined as a process which calls itself directly or indirectly and the corresponding function is called a recursive function.
# Iterative Walk Function:
# A program that iteratively and recursiley
# Iteratively walk function

print("Walking Fuction Using The Iterative Approach: ")
def walk_iteratively(steps):

    for step in range(1, steps+1):
        print(f'You take step #{step}')
walk_iteratively(20)

# Recursive: a  function calling itself from within
print("Walking Fuction Using The Iterative Approach: ")
def walk_recusive(steps):
    if steps == 0: # this line checks our base condition to let us know when to stop
        return # to exit a function / a base condition you can use return
    walk_recusive(steps - 1) # then we call the walk function again but pass in one less than the number we accepted
    print(f'You take step #{steps}')
walk_recusive(30)

# Stack Overflow Error In Recursive Functions:
'''
A recursive function that is called with an input that requires too many iterations will cause the stack to get to large, resulting in a stack overflow error.
When this happens it is more apporpriate to use an iterative solution. A recusive solution is only suited for a problem that does not exceed a certain number of recusive calls
'''
# Example of a Function that throws a stack overflow message:
def myfunction(n):
    if(n == 0):
        return n
    else:
        return myfunction(n-1)
#print(myfunction(1000)) # this function does a stack over flow

print()
print("Recursion and Nested Lists: ")
'''
A nested list can be traversed and flattened using a recursive function. The
base case evaluates an element in the list. If it is not another list, the single
element is appended to a flat list. The recursive step calls the recursive
function with the nested list element as input.
'''
def flatten(mylist):
    flatlist = []
    for element in mylist:
        if type(element) == list:
            flatlist += flatten(element)
        else:
            flatlist += element
    return flatlist
print(flatten(['a', ['b', ['c', ['d']], 'e'], 'f']))
print()
print("Fibonacci Recursion: ")
# A Fibonacci sequence is a mathematical series of numbers such that each
# number is the sum of the two preceding numbers, starting from 0 and 1.
# Ex. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
print("Using the Native Approach With a While Loop: ")
max = 15
num1 = 0
num2 = 1
next_num = num2
count = 1
while(count <= max):
    print(next_num,end=" ")
    count+=1
    num1, num2 = num2, next_num
    next_num = num1 + num2
print()
max1 = 15
num11 = 0
num21 = 1
next_num1 = num21
count1 = 1
print("Native Approach For-Loop Output (Done for mastery): ")
for num in range(max1):
    print(next_num1,end=" ")
    num11, num21 = num21, next_num1
    next_num1 = num11 + num21
print()
print("Fibonacci Recursion: ")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(12))
def summing():
    sum = int(0)
    altsumformasterypurposes = int(0)
    maxrange = int(input("Enter a max range for the numbers you want to sum up: "))
    while(maxrange < 0):
        maxrange = int(input("NO BICH ENTER A POSITIVE NUMBER: "))
    for numbers in range(maxrange + 1):
        sum += numbers
        altsumformasterypurposes = altsumformasterypurposes + numbers
    return (f"The is the sum of all the numbers up to {maxrange}: {sum}\n"
            f"This is the same sum of all the numbers up to {maxrange} but done differently: {altsumformasterypurposes}")
print(summing())
def printMultiplesOfN():
    dictionary = {}
    n = int(input("Enter a number you want to print the multiplies of(-1 to stop): "))
    maxrange = int(input(f"How many numbers do you want print that are multiples of {n} ?: "))
    while(n != -1):
        for multiples in range(maxrange+1):
            if(multiples % n == 0):
                print(multiples, end=" ")
        print()
        n = int(input("Enter a number you want to print the multiplies of(-1 to stop): "))
        maxrange = int(input(f"How many numbers do you want print that are multiples of {n} ?: "))
printMultiplesOfN()




print()
print("===========================================================================================================")
print()
print("Python Text Book Section 12.3 Examples of Recursive Algorithmns: \n")

def range_sum(num_list, start, end):
    if(start > end):
        return 0 # This functions base case is when the start parameter is greater the start parameter is greater than the end parameter, If true the function return the value 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)  # this statement returns that sum of num_list[start] plus the return value of a recursive call
    # Notice that in the recursive call the starting item in the range is start + 1.
    # in essence this statement is basically saying "return the value of the first item in the range plus the sum of the rest of the items in the range.
listofnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_sum = range_sum(listofnumbers, 3, 7)
print(f"My Sum: {my_sum}")
print()
print("===========================================================================================================")
print()
print("Finding the greatest common divisor: ")
# Our text task is to find the greater common divisor of two numbers:
#           - If x can be evenly divided into y, then god(x,y) = y
#           _ Otherwise, gcd(x,y) = gcd(y, remainder of x/y)
def GCD(x,y):
    if(x % y == 0):
        return y
    else:
        return GCD(x, x % y)
num11 = int(input("Enter a integer: "))
num222 = int(input("Enter another integer: "))
print(f"The greatest commond divisor of the two newly entered numbers is: {GCD(num11, num222)}")
print()
# The Tower Of Hanoi
# The Tower of Hanoi is a mathematical game that is often used in computer science to illustrate the power of recursion. The game uses three pegs and a set of discs with holes
# through their centers. The discs are stacked on one of the pegs:
# The discs are stacked on the leftmost peg, in order of size with the largest disc at the bottom.
# The game is based on a legend where a group of monks in a temple in Hanoi have a similar set of pegs with 64 discs.
#   The job of the monks is to move the discs from the first peg to the third peg.
#   The middle peg can be used as a temporary holder.
#   Futhermore, the monks follow these rules while moving the discs:
# ==========THE RULES OF THE GAME THAT THE MONKS MUST FOLLOW: ===================
# 1. Only one dick may be moved at a time
# 2. A disk cannot be placed on top of a smaller disc
# 3. All discs must be storaged on a peg except while being moved
# According to the legend, when the monks have all moved all their discs from the first peg to the last peg, the world will come to an end
#
# To play the game you must move all of the discs from the first peg to the third peg.
# Following the same rules as the monks. Lets look at some example solutions to this game, for different numbers of discs.
# If you only have one disc, the solution to the game is simple: move the disc from peg 1 to peg 3.
# But if you have 2 discs, the solution requires three moves:
# Move 1 - Move disc 1 to peg 2
# Move 2 - Move disc 2 to peg 3
# move 3 - Move disc 1 to peg 3
# Steps for moving three pegs:
#   1. Move disc 1 to peg 3.
#   2. Move disc 2 to peg 2.
#   3. Move dicc 1 to peg 2.
#   4. Move disc 3 to peg 3.
#   5. Move disc 1 to peg 1.
#   6. Move disc 2 to peg 3.
#   7. Move disc 1 to peg 3.
# This statement is summing up the general solution to problem: "Move N discs from peg 1 to peg 3 using peg 2 as a temporary peg".
# Describing What the recursive algorithm will be doing:
#   If  n > 0 :
#       Move n - 1 discs from peg A to peg B, using Peg C as a temporary peg
#       Move the remaining disc from peg A to Peg C.
#       Move n - 1 discs from peg B to Peg C, using peg A as the temporary peg
#
# The base case for the algorithm is reached when there are no more discs to move.
# The code is an implementation of what's above:
def move_discs(num, from_peg, to_peg, temp_peg):
    if (num > 0):
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print("Move a disc from peg", from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)


'''
num = The number of disc to move, 3
from_peg = The peg to move the discs from, 1
to_peg = The peg to move the discs to, 3
temp_peg = The peg we are using as the temporary peg, 2
'''
move_discs(3, 1, 3, 2)

print()


def tower_of_hanoi():
    num_disc = 3  # The total number of discs to move.
    from_peg = 1  # The peg to move the discs from.
    to_peg = 3  # The peg to move the discs to. #
    temp_peg = 2  # The peg to use a temporary peg which is peg # 2

    move_discs(num_disc, from_peg, to_peg, temp_peg)
    print("All the pegs are moved!!!")


tower_of_hanoi()
print()
print("Algoirithmn Work Bench using Recursion: ")
print("Practice Problem 1 Print Even and Odds Numbers Seperately using recusion\n"
      "\t-Only printing numbers from a minimum to a maximum from user input: ")
print()  # Spacing


# Python3 program to implement
# the above approach

# Function to print all the
# even numbers from L to R
def Even(L, R):  # Validating from left to right to check for evens
    # Base case
    if (R < L):
        return
    # Recurrence relation
    if (R % 2 == 0):
        Even(L, R - 2)  #IN side the parameters we re saying start looping at the minimum and
    else:
        Even(L, R - 1)
    # Check if R is even
    if (R % 2 == 0):
        print(R, end=", ")


# Function to print all the
# odd numbers from L to R
def Odd(L, R):  # Validating the numbers from LEFT to RIGHT in order to check for odds
    if (R < L):
        return  # Base case, meaning it will stop when the min value is greater than or equal to the maximum vaule
    # Recurrence relation
    if (R % 2 == 1):
        Odd(L, R - 2)
    else:
        Odd(L, R - 1)
    # Check if R is even
    if (R % 2 == 1):
        print(R, end=", ")  # This is where you print even numbers and check for validation


# Driver Code
def run():
    min = int(input("Enter a minimum: "))
    max = int(input("Enter a maximum: "))
    while (max < min):
        print("Maximum must be greater than the minimum for this to work ")
        max = int(input("Please try again: "))
    # Print all the
    # even numbers
    print("Even numbers: ", end=" ")
    Even(min, max)
    print(
        '\n------------------------------------------------------------------------------------------------------------------------------')

    # Print all the
    # odd numbers
    print(f"Odd numbers: ", end=" ")
    Odd(min, max)


run()
# Practice Problem 2: Print N to 1 without using a loop
print()
print("==============================================================")
print()
print("Practice Problem 2: Print N to 1 without using a loop: ")


def Nto1(n):
    if n > 0:
        print(n, end=', ')
        Nto1(n - 1)


n = 20
Nto1(n)
print("==============================================================")


def onetoN(n, y):
    if n < y + 1:
        print(n - 1, end=', ')
        onetoN(n + 1, y)


m = 1
y = 69
print()
print()
print("Practice Problem 3: Print One To N without using a loop: ")
onetoN(m, y)
print()
print("==============================================================")
print("Practice Problem 4: Printing One To N without using a loop a different way: ")


def onetoN2(n):
    if n > 0:  # Meaning this will go up to n
        onetoN2(n - 1)
        print(n, end=", ")


onetoN2(40)
print()
print()
print("Practice Problem 5: Product of 2 numbers using recursion: ")
def product(x,y):
    if(x<y):
        return product(y,x)
    elif( y != 0):
        return x+product(x, y - 1)
    else:
        return 0


x = 5
y = 2
print()
print(f'{x} x {y} => {product(x,y)}')
print()
print("Practice Problem 6: Printing the reverse of a string using recursion: ")
def reverseOfAString(string, length):
    if
# breakpoint()
#
#
# # Algorithm Work Bench :
# #
# def workbench1():
#     num = 0
#     show_sum(num)
#
#
# def show_sum(arg):
#     if (arg < 10):  # this is the value it loops up to which is 10 so it been 9 it would print 9
#         show_sum(arg + 1)
#     else:
#         print(arg)
#
#
# workbench1()
# print()
#
#
# def workbench2():
#     num = 0
#     show_sum2(
#         num)  # you are passing the variable num into the show_sum function and if that number is less than 9 is will print 9
#
#
# def show_sum2(arg):
#     if (arg < 9):  # this is the value it loops up to which is 9
#         show_sum2(arg + 1)  # this is the loop
#     else:
#         print(
#             arg)  # if the num in the workbench function where we called the show_sum(num) is greater than 9 then the function will print that value that is stored in num
#
#
# workbench2()
#
#
# def examplewhereitwontwork():
#     num = 20
#     show_sum2(num)  # note it printed 20 and not 10
#
#
# examplewhereitwontwork()
#
# work()
#
# breakpoint()
#
# # Example 2 Finding the factorial of a number: both iteratively and recursively
# print("Finding the factorial of number using the iterative approach: ")
#
#
# # The formula for factorial is n! = n*(n-1) * (n-2)*...*1
# def factorial_iterative(x):
#     result = 1
#     if x > 0:
#         for y in range(1, x + 1):
#             result *= y
#         return result
#
#
# print(factorial_iterative(20))
#
#
# def factorial_recusive(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial_recusive(x - 1)
#
#
# print(factorial_recusive(20))
# if (factorial_iterative(20) == factorial_recusive(20)):
#     print("It works")
# # Example 2: Write a recursive function that guven an input n, sums all nonnegative integers up to n.
# print()
# print("Example 2: Write a recursive function that guven an input n, sums all nonnegative integers up to n.")
#
#
# def sumMathematically(n):
#     return n * (n + 1) / 2
#
#
# def summing_iterative(n):
#     sum = int(0)
#     for num in range(n + 1):
#         sum += num
#     return f'This is the sum of all numbers up to {n}: {sum}'
#
#
# print(summing_iterative(20))
# print()
#
#
# def summing_recusive(n):
#     sum = int(0)
#     if (n == 0):
#         return 0
#     else:
#         return n + summing_recusive(n - 1)
#
#
# print(summing_recusive(5))
#
#
# #return f'{n} + {n-1} = {n+sum(n-1)}'
#
# # problem can be solved with recursion if it can be broken down into smaller problems that are identical in structure to the overall problem.
# def main():
#     num = int(input("Enter a nonnegative number: "))
#     while (num < 0):
#         num = int(input("Enter a nonnegative number luh nigga: "))
#     fact = factorial(num)
#     print(f'The factoiral of {num} is {fact}')
#
#
# def factorial(number):
#     x = number
#     if (number == 0):  # if n == 0 then, factorial(n) = 1
#         return 1
#     else:
#         return number * factorial(number - 1)
#
#
# main()
# print()
# print("===========================================================================================================")

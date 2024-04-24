
'''
 * Given base that is at least 0 and n, compute recursively (no loops) the value of base to the
 * n power, so powN(3, 2) is 9 (3 squared). Remember that any number to the 0 power will be 1.
 *
 * @param base
 * @param n power
 * @return result
 */
 '''
def powN(base, n):
    if n == 0:
        return 1
    else:
        return base * powN(base, n - 1)

# Example usage:
print(powN(3, 2))  # Output: 9




'''
 * Stephen gets easily distracted when browsing the internet. Every 15 minutes he spends
 * browsing he will open 3 more tabs. Given the current interval, recursively compute the total
 * number of tabs that Stephen will have open at the end of the current interval.
 *
 * Ex: (2 will be 6), (3 will be 9), (234 will be 702)
 *
 * @param t current intervals
 * @return amount of tabs open in 15 minutes time
'''
def tabs(t):
    if t == 0:
        return 0
    else:
        return 3 + tabs(t - 1)

# Example usage:
print(f"3 will be {tabs(3)}")  # Output: 9

'''
 * Deja tends to punctuate her sentences with far too many exclamation points. Write a recursive
 * method to tone them down a little bit.
 *
 * Given is a string of at least 1 character in length. Remove all but the last ! character from
 * the end of each. It is possible that there will be no ! characters at all, so a base case to
 * handle this will also be needed.
 *
 * Ex: "!String!!!" becomes "String!"
 *
 * @param str String
 * @return Edited string
'''
def overExclaim(string):
    if len(string) == 1 or string[-1] != '!':
        return string
    else:
        return overExclaim(string[:-1])

# Example usage:
print(f"!String!!! becomes {overExclaim('!String!!!')}")  # Output: "String!"
'''
 * Whenever Marquiss creates a screen name he adds an absurd amount of x characters (Upper and
 * Lowercase) throughout. Write a recursive method to count the total number of x characters
 * that Dante has added to his screen name.
 *
 * Ex: XxxRasenganxxX has 6, ThisxxxXxHas has 5, NothingHere has 0
 *
 * @param str value
 * @return result
'''
def manyX(string):
    if len(string) == 0:
        return 0
    else:
        count = 0
        if string[0] == 'x' or string[0] == 'X':
            count += 1
        return count + manyX(string[1:])

# Example usage:
strings = ["XxxRasenganxxX", "ThisxxxXxHas", "NothingHere"]
print(f"XxxRasenganxxX has {manyX('XxxRasenganxxX')}")
print("\n\n\n")
var1 = "governments"
var2 = "fair"
var3 = "humane"
print("May it be more {} and {} than the world your {} have made before.".format(var3, var2, var1))
'''
Probelm 1: 
Replacing Vowels with a *
You are going to write a program that takes a string called my_string and returns the string but with a * in the place of vowels. Assume that vowels are a, e, i, o, u. For example, if my_string = "Hello", then your program will print "H*ll*".
Important, the variable my_string is already declared as an empty string. Add a value to it and test your code. However, do not submit your code to be graded with the variable declaration. The auto-grader will declare the variable for you.
'''
def replace_vowels(my_string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in my_string:
        if char in vowels:
            new_string += "*"
        else:
            new_string += char
    return new_string

# Test the function
my_string = "Hello"
print(replace_vowels(my_string))  # Output: H*ll*
'''

Problem 2: 
Write a program that captures text from the user. Print the user string as many times as its length. Print as many lines of this as the length of the user input. Important, do not put a prompt when asking for user input. Just use input(). Adding a prompt will cause your program to not pass the tests.

Problem 3: 
Write a program that accepts input from the user. 
Create another string that contains either a u, l, or - for each character of the original string. 
Use u when the character is uppercase, and use l when the character is lowercase. 
If the character is neither uppercase or lowercase, use -. 
Print the second string. Important, do not put a prompt when asking for user input. 
Just use input(). Adding a prompt will cause your program to not pass the tests.
Expected Output
If the user inputs cat, then the output will be:
cat
lll

If the user inputs HouSE, then the output will be:
HouSE
ulluu


Problem 4: Problem
Write a program that takes input from a user. 
Print the first half of the string on one line, and the second half on another. 
In the case of a string that has an odd number of characters, the second line will have the extra character.
Important, do not put a prompt when asking for user input. Just use input(). 
Adding a prompt will cause your program to not pass the tests.

'''
'''

Select the appropriate code blocks that will create the list:

['Hello', 'Hello', 'Hello']

'''
my_list = ["Hello"]
print(my_list * 3)

'''
The In Operator:
The in operator tells you if a value is present in a list. in is a boolean operator, so it will return True or False.
The in operator returns a BOOLEAN value.
    The in operator returns a boolean value, which means either true or false.
'''
print("The In Operator: ")
print("\tExample: ")
my_list2 = ["red", "orange", "yellow", "green"]
print(f"\t\tPrinting if the color red is in the list above: {'red' in my_list2} ")

# The Append Method
# The append method adds an element to a list. append adds the element to the end of the list.
'''
The Sum Function & Strings:

You can concatenate strings with the + operator, which the same operator used to add numbers.
This may seem like it is possible to use the sum function with a list of strings. 
However, this will cause an error message
'''
print("The Sum Function and Strings: ")
my_list = [1, 2, 3, 4,5,6,7,8,9]
print(sum(my_list))
'''
The Min Function:
The min function is another built-in function that returns the minimum value of a list.
'''
def minandmaxfunction():
    print('The Min Function:')
    print("Example: \n")
    my_list = [45, 12, 9, 1]
    smallest = min(my_list)
    positonOfSmallest = my_list.index(smallest)
    print(f"The Smallest Element in {my_list} is {smallest} located at {positonOfSmallest}")
    fattest_fuck = max(my_list)
    positionOfFattestFuck = my_list.index(fattest_fuck)
    print(f"The Fattest Element in {my_list} is {fattest_fuck} located at {positionOfFattestFuck}")
minandmaxfunction()
#
movies = [
    ("The Lord of the Rings: The Return of the King", 11, 11),
    ("Titanic", 11, 14),
    ("Ben-Hur", 11, 12)
]

print(movies[1][2])

# 2D Lists
# Assume the following code:
print()
print("2D LISTS: ")
colors = [
           ["orange", "purple", "green"],
           ["blue", "white", "brown"],
           ["black", "red", "yellow"],
         ]
print("Which answer will print red?")
print(colors[2][1])
# The brackets are saying [list number 3][element number 2]
print("Which answer will print brown?")
print(colors[1][2])
'''
2D Lists
Assume the following code:
colors = [
           ["orange", "purple", "green"],
           ["blue", "white", "brown"],
           ["black", "red", "yellow"],
         ]
Drag the code blocks into the box below such that your program iterates over the 2D list and prints all of the elements. Hint: not all of the code blocks will be used.
'''
colors2 = [
           ["orange", "purple", "green"],
           ["blue", "white", "brown"],
           ["black", "red", "yellow"],
         ]
for row in colors:
    for color in row:
        print(color)

'''
Fill in the blanks below. Using the list my_list, complete the slice operator so that it returns [21, 17, 33].

my_list = [45, 99, 21, 17, 33, 7]
'''
a_list = [45, 99, 21, 17, 33, 7]
print(a_list[2:5])
print()
'''

The in Operator: 
    Create a program that prints True by dragging the appropriate code blocks to the box below. 
    You program must do the following things:
        1. Be two lines long
        2. Declare a list
        3. Print "True"
        4. Hint, not all of the code blocks will be used.
'''
my_list = [11, 71, 65, 42,3]
print(3 in my_list)
print()
'''
Changing a List
Write a program that takes a list of integers called numbers and will print a list with the elements odd or even based on the elements of numbers. For example, if numbers = [1, 2, 3, 4], then your program will print ['odd', 'even', 'odd', 'even'].
Important, do not edit the code in the top section. This code is necessary for the auto-grader to work. Add your code in the section below. Clicking the TRY IT button will test your code with numbers = [1, 2, 3, 4].

'''
# What will be the output to the following code?

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[::-1])
print()
neighborhood_dogs = ('Labrador Retriever', 'Yorkshire Terrier', 'Bulldog', 'Poodle', 'American Staffordshire Terrier', 'German Shepherd', 'Beagle', 'Corgi', 'Beagle', 'Dobermann', 'Bulldog', 'Siberian Husky', 'Rottweiler', 'Bulldog', 'Chihuahua', 'Boxer', 'Dachshund', 'Great Dane', 'Bulldog', 'Pug')
print(neighborhood_dogs.count('Bulldog'))
friends_in_city = ((4, 'Austin'), (9, 'San Francisco'), (6, 'New York'), (2, 'Seattle'))
for index, info in enumerate(sorted(friends_in_city, key=lambda element: element[0])):
  friends, city = info
  print(friends, city)
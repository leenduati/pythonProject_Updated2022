# Output something to the screen
print("hello world")

result = 64
print(int(result) ** 5)

# Separate two variable names using _ e.g. new_name_assigned = 43
# Strings are a sequence of characters. String methods
# Use double or single quotes
"""
This is a comment
Multi line comments

"""
lee = "My name is lee Nduati, a fan of Ng'olo"
print(lee.find("y"))
print(lee.count("O"))
# Slicing
print(lee.split(" "))
print(lee[-1])
print(lee[10:])
print(lee[:3])
# Recommend step size by:
print(lee[::2])
#  Strings are immutable,
print(lee.upper())
new_string = "and also Mason Mount"
print(lee.join(new_string))
print("{} and {}".format(lee, new_string))
print("insert string here {}".format(lee))
print("Item one is {x} and item two is {y}".format(x="cat", y="dog"))

# Python LISTS called arrays in JS, lists are mutable
my_list = [1, "hello", True, False, [88, 999, -1, "a"]]
print(len(my_list[-1]))
my_list[2] = "truth"
print(my_list)
my_list.append("haha")  # add item to last of string
print(my_list)
second_list = [5, 4, 21]
my_list.extend(second_list)  # add another list to initial list
print(my_list)
# remove last item frm list using .pop
my_list.pop()
#  specify index of where to pop item by
my_list.pop(3)
print(my_list)
my_list.reverse()  # reverse string
# my_list.sort()  sort will not work here due to different data types
print(my_list)

# List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for jelly in matrix:
    print(jelly)

# This prints out first item in each nested list
first_col = [row[0] for row in matrix]

print(first_col)

# Dictionaries, allow users to create a "mapping" with key-value pairs
my_stuff = {
    "key1": "value1",
    "key2": 8,
    "key3": True,
    "key4": [1, 2, 3, 4, 5],
    3: 55,
    True: "truth"
}

print(my_stuff[True])
my_stuff.values()

for keys, values in my_stuff.items():
    print(keys, values)

# print(my_stuff["0"])

# Tuples, are immutable, sets are unordered collections of unique elements, boolean are Tre/False
#  Boolean are true or false
coordinates = (1, 2, 3, "a", True, "123")
print(coordinates[0])
# Sets
x = set()
x.add(4)
x.add(22)
print(x)
# Set is a unique element, so multiple inputs will only be printed once

# Exercise 1
#####################################
# PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

print("Start of exercise questions")
###############
# Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[-1:-3])
# Bonus: Use indexing to reverse the string
print(s[::-1])

print("End of Problem 1 ")
###############
# Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print(l)
print("End of problem 2 ")
###############
# Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
print(d1["simple_key"])
d2 = {'k1': {'k2': 'hello'}}
print(d2["k1"]["k2"])
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3["k1"][0]["nest_key"][1])

print("End of problem 3 ")
###############
# Problem 4 ##
###############

# Use a set to find the unique values of the list below:
my_set = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
my_set = set(my_set)
print(my_set)
print("End of problem 4")
###############
# Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {} and he is {} years old".format(age, name))

# Loops, if, if else, elif, else
#  and or
if age > 2:
    print("age is {}".format(age))
else:
    print("age is not greater than 2")

# Iterate through a tuple


my_pairs = [(1, 2), (3, 4), (5, 6)]
for i in my_pairs:
    print(i)

for tup1, tup2 in my_pairs:
    print(tup1, tup2)

# While loops in python
y = 0
while y < 5:
    print("i is {}".format(y))
    y = y + 1

# use range to generate lists
print(range(5))
# Use range to generate simple lists Python’s enumerate() lets you write Pythonic for loops when you need a count and
# the value from an iterable. The big advantage of enumerate() is that it returns a tuple with the counter and value,
# so you don’t have to increment the counter yourself. It also gives you the option to change the starting value for
# the counter.
l2 = ["lee", "nduati", "francis"]
l2_en = enumerate(l2, 5)
# Include number at end function to be the starting point of enumerate function
for l in l2_en:
    print(l)

# List comprehension
num = [1, 2, 3]
out = [x ** 2 for x in num]
print(out)


# Functions in Python
def name():
    """
    THis is the docstring. Use docstrings in python
    :return:
    """
    print("THis is a function")


name()
# Check type of output using type()
type(5)
type("string")


# Lambda expressions
# 1. Filter
def even_fil(n):
    return n % 2 == 0


result = filter(even_fil, num)
print(list(result))

# Lambda expression has no name, also called an anonymous function
# No need to define an entire function if itis used only once
# Hence we write
var = lambda no: no % 2 == 0
result1 = filter(var, num)
print(list(result1))

print("x" in [1, 2, 3, 45, 5])

# Function Exercises
#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True


def arrayCheck(nums):
    result3 = ""
    for index in nums:
        result3 = result3 + str(index)
    return "123" in result3
# CODE GOES HERE



#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(s):
    result5 = ""
    for r in range(len(s)):
        if r % 2 == 0:
            result5 = result5 + s[r]

    print(result5)


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    return b.lower() in a.lower() or a.lower() in b.lower()
  # CODE GOES HERE

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(st):
    # To turn this into a list
    # result4 = [res*2 for res in st ]
    # print(result4)
    result4 = ""
    for res in st:
        result4 = result4 + res * 2

    print(result4)
  # CODE GOES HERE


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    sum1 = 0
    if (a or b or c != 13) or () :
        sum1 = a + b + c



  # CODE GOES HERE

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count + 1

    return count
  # CODE GOES HERE

import random
random.randint(2,3)



###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

# Another hint:
guess = input("What is your guess? ")
print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!


# Start of exercise

import random
import math

print(random.randint(1, 2))


def lee():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    result = str(num1) + str(num2) + str(num3)
    return result


n = lee()


def ran():
    result = ""
    ans = int(input(("Enter numbers: ")))
    if len(n) != len(set(n)):
        lee()
    else:
        print(n)
        a = list(str(ans))
        na = list(n)
        for i in a:
            for j in na:
                if a[int(i)] == na[int(j)]:
                    result = "close"
                    print(i, j)
                    print(result)


ran()


# End of exercise
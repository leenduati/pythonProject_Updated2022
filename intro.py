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
    print( jelly)


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
l[2][2] ="goodbye"
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
out = [x**2 for x in num]
print(out)
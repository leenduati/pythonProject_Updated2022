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


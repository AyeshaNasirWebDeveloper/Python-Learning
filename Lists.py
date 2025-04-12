# ***Control Flow***

#Comparison Operators
# Comparison operators are used to compare values and return True or False. Here are the most common ones:

# == (equal to)
# !=  (not equal to)
# >   (greater than)
# <   (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

a = 10
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  #False

# Logical Operators & Condional Statements

# Logical operators combine multiple conditions:

# and (True if both conditions are True)
# or (True if at least one condition is True)
# not (reverses the result of a condition)

prompt = int(input("Enter Your age: "))

if prompt >= 18 and prompt <= 60 :
  print("You are eligible for licence")
elif prompt >= 60 and prompt <= 100:
  print("You already have a license and you are a senior citizen so you can drive")
else:
  print("You are not eligible for license")



signal_lights = ["red", "yellow", "green"]

if "red" in signal_lights:
  print("Stop")
elif "yellow" in signal_lights:
  print("Get Ready")
else:
  print("Go")

# Match Cases

# The match-case statement works by comparing an expression against multiple patterns. The syntax is:

def get_grade(score):
    match score:
        case score if score >= 90:
            return "A+"
        case score if score >= 80:
            return "A"
        case score if score >= 70:
            return "B"
        case score if score >= 60:
            return "C"
        case score if score >= 50:
            return "D"
        case _:
            return "F"

score = int(input("Enter Your Score: "))
print(get_grade(score))

"""# ***Loops & Iteration***"""

# Loops

# For Loop

#  loop with range method
prompt = input("Enter a message!")

for i in range(5):
  print(prompt)

# loop with else
signal_colors = ["red", "yellow", "green"]

for color in signal_colors:
  print(color)
else:
    print("No more colors")

# loop with break keyword
num = [10, 20, 30, 40, 50]

for i in num:
  if i == 30:
    break
    print(i)
  else:
    print(i)


  # Searching with Else
colors = ["red", "yellow", "green"]

for color in colors:

  if "orange" == color:
    print("Color Found")
else:
    print("Not Found")


# Finding Odd Numbers
for i in range(1, 51, 2):
  print("Odd Number is: ", i)


# Throwaway variable (_) underscore
# We don't plan to use

prompt = input("Enter a fruit Name ")
for _ in prompt:
  print(prompt)


# While Loop

i = 0
while i< 5:
  i +=1
  print(i)

# loop with break
i = 0
while i < 5:
  i += 1
  if i == 3:
    break
  print(i)

# loop with continue
i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)


# Multiplication Table

for i in range(1,11):
  print(f"Multiplication Table of {i}")
  for j in range(1,11):
    print(f"{i} x {j} = {i * j}")

"""# ***Lists, Tuples & Dictionaries***

# ***List***
"""

from __future__ import division
# Lists

fruits: list = ["mango", "kiwi", "grapes", "watermelon", "apricot"]

print(fruits) # list

print(fruits[1]) # access element

modify= fruits[-1] = "cherry"
print(fruits) # modified

print(fruits[0:2]) # slicing


# List Methods

# append is used for adding a value in the end
last_add = fruits.append("apple")
print(fruits) # it prints full list of fruit

# extend is used for adding multiple elements
multiple_add = fruits.extend(["banana", "orange"])
print(fruits) # it prints full list of fruit


# Remove() Method

# The remove() method is used to delete the first occurrence of a specified value from a list. If the value is not found in the list,
# a ValueError exception is raised.

fruits.remove("cherry")
print(fruits)


# Pop() Method

# The pop() method is used to delete an item at a specified index from a list. If no index is provided, it removes and returns the last item in the list.
# If the index is out of range, an IndexError exception is raised.

fruits.pop(0)
print(fruits)

# Sort Default Ascending Order
numbs :list[int] = [5, 9, 7, 2, 6, 1, 4, 2, 3, 8]
print(numbs)
# sorting
numbs.sort()
print(numbs)

# Sort Descending Order
numbs.sort(reverse=True)
print(numbs)

# sort by lenght
fruits.sort(key=len)
print(fruits)

# Sorting by last character
fruits.sort(key=lambda x: x[-1])
print(fruits)

# Reverse
fruits.reverse()
print(fruits)

# Iterating over lists
for _ in fruits:
  print(_)

# list comprehension

# List comprehension is a powerful feature in Python that allows you to create new lists in a concise and readable way. It's a compact way to create lists from existing lists or other iterables by applying a transformation or filter to each element.

# new_list = [expression for element in iterable if condition]

# expression is the operation you want to perform on each element.
# element is the variable that takes on the value of each element in the iterable.
# iterable is the list or other iterable that you want to process.
# condition is an optional filter that determines whether an element is included in the new list.

# without condions
additon : list[int] = [i + 10 for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(additon)
multiplifcation: list[int] = [i * 10 for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(multiplifcation)
division: list[int] = [i / 10 for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(division)
subtraction: list[int] = [i - 10 for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(subtraction)

# With Conditions
# even numbers
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print("Even Number: ",even_numbers)

# odd numbers
odd_numbers = [i for i in range(0, 12) if i % 2 != 0]
print("Odd Number: ", odd_numbers)

# List comprehension is commonly used for:

# Transforming data: List comprehension can be used to transform data from one format to another.
# Filtering data: List comprehension can be used to filter out unwanted data.
# Creating new data: List comprehension can be used to create new data by combining existing data.

"""# ***Tuples***"""

names : tuple = ("Ayesha", "Rohma", "Mehmoona", "Urooj", "Yousra")
print(names)

# unique hash values
nums1 : tuple = (1,2,3)
nums2 : tuple = (1,2,3)
nums3 : tuple = (1,2,3)

# all same
print(hash(nums1))
print(hash(nums2))
print(hash(nums3))

# all different
print(id(nums1))
print(id(nums2))
print(id(nums3))

print("checking equality: ", nums1 == nums2 )
print("checking equality: ", nums1 == nums3 )

# Why are Tuples Immutable?

# There are several reasons why tuples are immutable:

# Memory Efficiency: Immutable tuples can be stored in a single block of memory, which makes them more memory-efficient than lists.
# Thread Safety: Immutable tuples are thread-safe, meaning that they can be safely accessed and shared between multiple threads without fear of modification.
# Hashability: Immutable tuples are hashable, meaning that they can be used as keys in dictionaries.

print(names[0]) # accessing first element
print(names[-1]) # accessing last element

# slicing
print(names[4])
print(names[:3])
print(names[1:])
print(names[-1])

# lenght
print(len(names))

# iterating through a tuple
for name in names:
  print(name)

# availabilty checking
print("Urooj" in names)

# concatenating tuples
names_with_nums: tuple = names + nums1 + nums2 + nums3
print(names_with_nums)

# repeating tuples
nums4 : tuple = nums1 * 3
print(nums4)

# Nested Tuples
nested_tuples : tuple = (names, nums1, nums2, nums3)
print(nested_tuples)

# unpacking tuples
name1, name2, name3, name4, name5 = names
print(name1, name2, name3, name4, name5)
print(names)

# in dictionary tuples works as a key because it is immutable and ordered
dictionary: dict = {"tup1": "This is a tuple one value!", "tup2": "This is a tuple two value!", "tup3": "This is a tuple three value!"}
print(dictionary)

#Trying to modify a tuple will result in a TypeError
# tuple1[0] = "watermelon" #immutable. This line will raise an error. Uncomment to test.

# Tuple Methods
print(names.count("Ayesha")) #1
print(names.index("Ayesha")) #0

tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]
print(tuple_methods)

# Type Hint
inp : bool = input("Enter Your Good Name! ")
print(inp)
print(type(inp))

"""# ***Dictionary***"""

dictionaryy : dict = {
    "name": "Ayesha Nasir",
    "roll-no": 12345,
    "batch": 1,
    "quarter-no": "Q3",
    "course": "AI, Web 3.0 & Metaverse"
}
print(dictionaryy)

# accessing value
print(dictionaryy["name"])
print(dictionaryy["roll-no"])

# get method
print(dictionaryy.get("name"))
print(dictionaryy.get("department", "GIAIC")) # Key not found! thats why GIAIC is the output

# adding in dictionary
dictionaryy["email"] = "ayeshanasir@gmail.com"
print(dictionaryy)

# modifying
dictionaryy["name"] = "Ayesha"
print(dictionaryy)

# deleting the key and value
del dictionaryy['email']
print(dictionaryy)

# pop method
dictionaryy.pop("name")
print(dictionaryy)

# popitem method
dictionaryy.popitem()
print(dictionaryy)

# Remove a key-value pair using pop
age: int = dictionaryy.pop("age", -1)
print("Removed age:", age)
print(dictionaryy)

print("\n-----\n")
#Again remove a key which is already removed to check the default value
age: int = dictionaryy.pop("age", -1)
print("key 'age' not found in dict so returning default value: ", age)


# Dictionary Methods
# Python provides several useful methods for working with dictionaries.

# Method	Description
# keys()	Returns a list of all keys in the dictionary.
# values()	Returns a list of all values in the dictionary.
# items()	Returns a list of key-value pairs as tuples.
# clear()	Removes all items from the dictionary.
# update()	Adds or updates multiple key-value pairs from another dictionary.
# copy()	Creates a shallow copy of the dictionary.
# get()	Returns the value for a given key, or a default value if the key is not found.

print(dictionaryy.keys())
print(dictionaryy.values())
print(dictionaryy.items())
print(dictionaryy.clear())
print(dictionaryy.update({"name": "Ayesha Nasir"}))
print(dictionaryy.copy())
print(dictionaryy.get("name"))

# dictionary methods
dictionary_methods: list = [method for method in dir(dict) if not method.startswith('__')]
print(dictionary_methods)

# iterating in dictionary

for key in dictionaryy:
  print(key)

for value in dictionaryy.values():
  print(value)

for key, value in dictionaryy.items():
  print(key, value)

"""# ***Sets***"""

# A set is:

# unordered
# unchangeable
# unindexed
# mutable
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

sets : set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 8, 5, 2, 4, 6}
print(sets)

empty_set: set = set()

# A set can store only immutable objects such as number (int, float, complex or bool), string or tuple.
# If you try to put a list or a dictionary in the set collection, Python raises a TypeErro

# multiple data type holding
multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1,5,9,'hi') }
print(multi_type_set)

languages:set= {"Java", "JavaScript", "Python", "C#", "C++"}
print(languages)


# ***Variables***

name = "Ayesha Nasir"
print("Full Name: ", name)
education = "BBA"
print("Education: ", education)
hobby = "Explore New things"
print("Hobby: ", hobby)


# **Data Types**

# Integers
num: int = 20
print(num)
print("Type of Number: ", type(num))

# String
name: str = "Ayesha"
print(name)
print("Type of Name: ", type(name))

# Float
floating_Num: float = 2.05
print(floating_Num)
print("Type of Floating Number: ", type(floating_Num))

# Boolean
isTrue: bool = True
print(isTrue)
print("Type of isTrue: ", type(isTrue))

isFalse: bool = False
print(isFalse)
print("Type of isFalse: ", type(isFalse))

# List
fruits: list = ["Apple", "Mango", "Banana", "Cherry", "Strawberry"]
print(fruits)
print("Type of fruits: ", type(fruits))

# Tuple
veggies: tuple = ("Potato", "Tomato", "Onion", "Garlic", "Lady Finger")
print(veggies)
print("Type of veggies: ", type(veggies))

# Dictionary
studentDetails: dict = {
    name: "Ayesha Nasir",
    education: "BBA",
    hobby: "Explore New things",
    id: 1,

}
print(studentDetails)
print("Type of studentDetails: ", type(studentDetails))

# Set
numbers: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numbers)
print("Type of numbers: ", type(numbers))

# None
nothing: None = None
print(nothing)
print("Type of nothing: ", type(nothing))

# Frozen Set
frozenSet: frozenset = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(frozenSet)
print("Type of frozenSet: ", type(frozenSet))

"""#**Case Sensitive**"""

# Small "p" and Capital "P" are different
# Both are Different
product:str="Food Panda"
Product:str="Deal Cart"
print(product)
print(Product)

"""## **Comment**"""

# It is use for Single Line Comment
""" It is use for Multi Line Comment """

"""# ***Special Keywords***"""

import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

"""# ***Understanding Keywords***

## ***Value Keywords***
"""

#Value Keywords
True, False, None

# True, False: #These represent a boolean values.

# None: #This is a special constant used to denote a null value or a void. It’s important to remember that 0, any empty container(e.g. empty list) does not compute to None. It is an object of its datatype – NoneType. It is not possible to create multiple None objects and can assign them to variables.

print(False == 0) #True

print(True == 1) #True

print(None == 0) #False

print(None == []) #False

"""## ***Operator Keywords***"""

#Operator Keywords
# and, or, not, in, is

# and Keyword – return ‘True’ if both the operands are ‘True’
# or Keyword – return ‘True’ if at least one operand is ‘True’
# not keyword – returns ‘True’ if the expression is ‘False’, and vice versa.

"""### ***Logical Operators***"""

a = True
b = False

# Logical operations:
# and or not

print(a and b)  # AND: True if both a and b are True
print(a or b)   # OR: True if at least one of a or b is True
print(not a)    # NOT: Inverts the value of a

"""### ***Membership Operators***"""

# in Keyword

# Check if a value exists in a sequence (like a list, tuple, or string). It returns True if value is found.

print(3 in [1,2,3]) #True

if 's' in 'Ayesha Nasir':
    print("s is part of Ayesha Nasir")
else:
    print("s is not part of Ayesha Nasir")

#is Keyword

# Check if two variables point to the same object in memory. It returns True if the objects are identical.
print(2 == 2)
print(2 is 2)

# Check if two objects are the same object:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# True: a and b refer to the same object
print(a is b)

# False: a and c have same value but are different objects
print(a is c)

"""## ***Control Flow Keywords***"""

# Control Flow Keywords
# if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert

"""### ***Conditional Keywords***"""

age = int(input(("Enter Your Age!")))
if age >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")

# python if elif else statement
user_input = input("Enter your Signal Light Colour!")
if user_input == "red":
    print("Stop")
elif user_input == "yellow":
    print("Slow")
elif user_input == "green":
    print("Go")
else:
    print("Invalid")

"""### ***Iteration Keywords***"""

# 'for' loop example
for num in range(3):
    if num == 2:
        continue  # Skip number 2
    print(num)
# Output: 0 1

# 'while' loop example
count = 0
while count < 4:
    count += 1
    if count == 3:
        break  # Exit the loop when count reaches 4
    print(count)
# Output: 1 2

n = 10
for i in range(n):

    # pass can be used as placeholder
    # when code is to added later
    pass

"""### ***Exception Error Handling Keywords***"""

# try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.
# except : As explained above, this works with “try” to catch exceptions.
# finally : No matter what is result of the “try” block, “finally” is always executed.
# raise: We can raise an exception explicitly with the raise keyword
# assert: This function is used for debugging purposes. Usually used to check the correctness of code. If a statement is evaluated to be true, nothing happens but when it is false, ” AssertionError ” is raised. One can also print a message with the error, separated by a comma .

a, b = 4, 0
print(a , b)


try:
    k = a // b  # Attempt integer division (4 // 0)
    print(k)

# This block catches the ZeroDivisionError
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # This block is always executed regardless of the exception
    print('This is always executed')


print("The value of a / b is : ")

# Will raise an AssertionError because b == 0
assert b != 0, "Divide by 0 error"

# Division is attempted but will not reach due to assert
print(a / b)

# Raise a TypeError if the strings are different
temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different.")

"""***del keyword***"""

# del is used to delete a reference to an object. Any variable or list value can be deleted using del.

variable = "Ayesha Nasir"
print(variable)
del variable
print(variable) #Name Error

"""## ***Structured Keyowrds***"""

# Function and Class
# def, return, lambda, yield, class

#def keyword is used for making the function in python
def name():
  print("Hello! My name is Ayesha Nasir")

name()

# class keyword is used to declare user defined classes.
class data:
  name= "Ayesha Nasir"
  education= "BBA"
  hobby= "Explore New things"
  interest= "Machine Learning"
  favouritesubject= "Data Science"
  print(data.name)
  print(data.education)
  print(data.hobby)
  print(data.interest)
  print(data.favouritesubject)


  # Return and Yield Keyword use in Python


# The ‘return' keyword is used to return a final result from a function, and it exits the function immediately. In contrast, the ‘yield' keyword is used to create a generator, and it allows the function to yield multiple values without exiting. When ‘return' is used, it returns a single value and ends the function, while ‘yield' returns multiple values one at a time and keeps the function’s state.

# Return keyword
def num():

     # Assign the value 2 to variable S
    nums = 2

    # Return the value of S
    return nums

# Call the function and print the result
print(num())

# Yield Keyword
def fun():

      # Yield the value 1, pausing the function here
    yield 1
    # Yield the value 2, pausing the function again
    yield 2
    # Yield the value 3, pausing the function once more
    yield 3

# Iterate through the values yielded by the function
for value in fun():
    print(value)



    # Lambda keyword is used to make inline returning functions with no statements allowed internally.

    # Lambda keyword
power = lambda x: x*x*x

print(power(2))

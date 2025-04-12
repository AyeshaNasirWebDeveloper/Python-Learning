# ***Operators***
#There are seven operators in Python

# * Arithmetic Operators.
# * Comparison (Relational) Operators.
# * Assignment Operators.
# * Logical Operators.
# * Bitwise Operators.
# * Membership Operators.
# * Identity Operators.

# ***Arithemetic Operators***

# Arithmetic operators are used with numeric values to perform common mathematical operations:

# * Addition	x + y
# * Subtraction	x - y
# * Multiplication	x * y
# * Division	x / y
# * Modulus	x % y
# * Exponentiation	x ** y
# * Floor division	x // y
"""

# Arithemetic Operators

x =10
y = 5

print(x+y) #Output: 15           #Addition
print(x-y) # Output: 5           #Subtraction
print(x*y) #Output: 50           #Multiplication
print(x/y) #Output: 2            #Division
print(x%y) #Output: 0            #Modulus
print(x**y) #Output: 100000      #Exponentiation
print(x//y) #Output: 2.0         #Floor Division

"""
# ***Comparison (Relational) Operators.***
# Comparison operators are used to compare two values:

# * Equal	x == y
# * Not equal	x != y
# * Greater than	x > y
# * Less than	x < y
# * Greater than or equal to	x >= y
# * Less than or equal to	x <= **y**
# """

#Comparison (Relational) Operators

x = 50
y = 10

print(x==y) #Output: False
print(x!=y) #Output: True
print(x>y)  #Output: True
print(x<y)  #Output: False
print(x>=y) #Output: True
print(x<=y) #Output: False

"""# ***Assignment Operators***
Assignment operators are used to assign values to variables:
"""

# Assignment Operators

x = 30
print(x) #Output: 30

x += 5
print(x) #Output: 35

x -= 5
print(x) #Output: 30

x *= 5
print(x) #Output: 150

x /= 5
print(x) #Output: 30.0

x %= 5
print(x) #Output: 0.0

x // 7
print(x) #Output: 0.0

x **= 5
print(x) #Output: 0.0

# x &= 3
print(x) #Output: 0.0

# x |= 3
print(x) #Output: 3.0

# x ^= 3
print(x) #Output: 3.0

# x >>= 5
print(x) #Output: 0.0

# x <<= 5
print(x) #Output: 0.0

# x := 8
print(x) #Output: 8

"""# ***Logical Operators***
Python logical operators (and, or, not) are special keywords that act as conjunctions in our code, connecting and evaluating multiple conditions within a single expression.

* and
* or
* not
"""

# Logical Operators

a = 5
b = 4

print(a >= b and a > b) # Output: True
print(a < b or a > b) # Output: True
print(not(a == b and a > b)) # Output: True

"""# ***Bitwise Operators***
Bitwise operators are used to compare (binary) numbers:

* & 	AND	Sets each bit to 1 if both bits are 1	x & y
* |	OR	Sets each bit to 1 if one of two bits is 1	x | y
* ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
* ~	NOT	Inverts all the bits	~x
* <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
* Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

"""

# Bitwise Operators

a = 10
b = 5

print(a == b & a > b) # Output: False
print(a < b | a > b) # Output: True
print(not(a == b & a > b)) # Output: True
print(a ^ b) # Output:  15
print(~a) # Output: -11
print(a << b) # Output:  320
print(a >> b) # Output:  0

"""# ***Membership Operators***
Membership operators are used to test if a sequence is presented in an object:

* in 	Returns True if a sequence with the specified value is present in the object	x in y

* not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""

# Membership Operators

fruits = ["Strawberry", "Apple", "Banana", "Cherry", "Dragon Fruit"]

print("Apple" in fruits) # Output: True
print("Mango" not in fruits) # Output: True

"""# ***Identity Operators***

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

* is 	Returns True if both variables are the same object	x is y
* is not	Returns True if both variables are not the same object	x is not y
"""

# Identity Operators

x = ["Strawberry", "Apple", "Banana", "Cherry", "Dragon Fruit"]
y = ["Strawberry", "Apple", "Banana", "Cherry", "Dragon Fruit"]
z = x

print(x is z) # Output: True
print(x is y) # Output: False
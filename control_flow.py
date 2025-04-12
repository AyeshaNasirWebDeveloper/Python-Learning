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


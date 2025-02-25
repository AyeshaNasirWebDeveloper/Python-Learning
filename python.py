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
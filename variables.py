"""
This is a multiline comment 
or docstring. 
single or double quotes can be used 
"""

# This is a single line comment 

"""
Variable rules:
- Variable names are case sensitive 
- Variables must start with a letter or an undersocre
- Can have numbers but can not start with one. 
"""

# x = 1 # int 
# y = 2.5 # float
# name = 'Zachary' # str

# is_cool = True # bool


# Multiple assignment 
x,y,name,iS_cool = (1, 2.5, 'Zachary', True)

# print(x) # prints x 
# print(x,y,name,iS_cool) # prints out all of the variables defined above 

# Basic math 
a = x +y 
# print(a) # prints the sum of x and y 

# print(type(x)) # gives us the type of variable x 

# Casting X to a string 
x = str(x) # converts x to a string
y = int(y) # converts y into a int
z = float(y) # converts an int to a float 
print(type(x))
print(type(y),y)
print(type(z),z)

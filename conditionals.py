"""
If / Else conditions are used to decide to do something based on something being either true or false 
"""

x = 2 
y = 20


"""
Comparison operators are used to compare values 
"""

# If else 
# if x > y: 
#     print(f'{x} is greater than {y} ')
# else: 
#     print(f'{y} is greater than {x}')


# elif 
# if x > y: 
#     print(f'{x} is greater than {y} ')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else: 
#     print(f'{y} is greater than {x}')


# Nested If 

# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less then or equal to 10 ')


"""
Logical operators are used to combine conditional statements 
"""

# and
# if x > 2 and x <=10:
#     print(f'{x} is greater than 2 and less than or equal to 10')

# or
# if x > 2 or x <=10:
#     print(f'{x} is greater than 2 or less than or equal to 10')

# not 
# if not(x ==y):
#     print(f'{x} is not euqal to {y}')



"""
Membership operators are used to test is a sequence is present in an object. 
"""

numbers = [1,2,3,4,5]

# in 
# if x in numbers:
#     print(x in numbers)


# not in 

# if x not in numbers:
#     print(x  not in numbers)

"""
Identity operortors compare the objects not if they are equal but if they are acutally the same object, with the same memory location. 

"""

# is 
if x is y:
    print(x is y)

# is not 
if x is not y:
    print(x is not y)
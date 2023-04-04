"""
A function is a block of code which only runs when it is called upon. 
In python we use indentation with tabs or spaces 
"""

# Create a function

def sayHello(name):
    print(f'Hello {name}')

# sayHello('Zachary')

# return values 
def getSum(num1, num2):
    total = num1 + num2 
    return total

num = getSum(3,4)
# print(num)

"""
A lambda functino is a small ananomous functin 
A lambda function can take any number of arguments, but can only have one expression. 
"""
getSum = lambda num1, num2 : num1 + num2 

print(getSum(10,3))


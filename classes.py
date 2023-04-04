"""
A class is like a blueprint for creating objects. 
An object has properties and methods associated with it.
"""

# create class
class User:
    # Constructer
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age 
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age +=1

# Extend class
class Customer(User):
     def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age 
        self.balance = 0 
     def set_balance(self,balance):
        self.balance = balance    
     def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my blance is {self.balance}'

# Init user object 
zachary = User('Zachary Anstey', 'zachary.anstey@gmail.com',25)

# Init Customer object 
zachary = Customer('Zachary','zachary.anstey@gmail.com',25)
zachary.set_balance(500)
print(zachary.greeting())

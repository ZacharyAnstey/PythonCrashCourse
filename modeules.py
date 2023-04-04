"""
A module is a file contanint a set of functions to include in your application. 
There are core python modules, and modules that you can install using pip
"""
# c ore modules 
import datetime
from datetime import date
import time
from time import time


# pip module 
import camelcase
from camelcase import CamelCase


# custom module 
import validator
from validator import validate_email

today = date.today()
# print(today)

timestamp = time()

c =CamelCase()
# print(c.hump('hello there world'))

email = 'test@test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad ')
# print(timestamp)
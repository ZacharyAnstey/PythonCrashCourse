# A dictionary is a collection which is unordered, changable, and indexed. No duplicate members 

# create a dictionary 

person = {
    'first_name': 'Zachary',
    'last_name': 'Anstey',
    'age' : 25
}

# use a constructor 
person2 = dict(first_name='John',last_name='doe')

# print(person2,type(person))
# print(person, type(person))


# Get value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key/value

person['phone'] = '555-555-55555'
# print(person)

# Get dict keys 
# print(person.keys())

# get dict items 
# print(person.items())

# copy dirct
person2 = person.copy()
person2['city'] = 'Boston'
# print(person2)

# remove item 
del(person['age'])
person.pop('phone')
# print(person)


# Clear
person.clear()
# print(person)

# Get length
print(len(person2))

# List of dictionaries 
people = [
    {'name':'Martha','age':30},
    {'name': 'Kevin','age':25}
]
print(people[1])

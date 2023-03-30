# A tuple is a collection that is unordered and unmutable 

# Create tuple 
fruits = ('apples', 'oranges','grapes')
fruits2 = tuple(('apples','oranges','grapes'))

# print(fruits,fruits2)

# Single values need to have a traling comma 
fruits3 = ('apples',)

# print(fruits3,type(fruits3))

# get value
# print(fruits[1])


# can't change value
# fruits[0] = 'pears' # gives error 

# Delete tuple 
del fruits3
# print(fruits3)

# find len of tuple 
# print(len(fruits))


# A set is a collection that is unordered and unindexed 


# Create a set 
fruits_set = {'apples','oranges','mango'}

# check is in set
# print('apples' in fruits_set)

# Add to set 
fruits_set.add('grape')
# print(fruits_set)

# remove from set 
fruits_set.remove('grape')
print(fruits_set)

# clear set 
fruits_set.clear()
# print(fruits_set)

# delete 
del fruits_set

# print(fruits_set)
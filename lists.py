# Data type 
# ordered 


# Create a list 
numbers = [1,2,3,4,5]
fruits = ['apples','oranges','grapes','pears']
# use a constructer
numbers2 = list((1,2,3,4,5))

# print(numbers,numbers2)

# Get a value 
# print(fruits[1])

# Get the lengths of the list 
# print(len(fruits))

# Append 
fruits.append('mangos')
# print(fruits)

# remove 
fruits.remove('grapes')
# print(fruits)

# insert 
fruits.insert(2,'strawberries')
# print(fruits)

# remove with pop
fruits.pop(2)
# print(fruits)

# reverse list 
fruits.reverse()
print(fruits)

# Sort lsit 
fruits.sort()
# print(fruits)

# reverse sort
fruits.sort(reverse=True)
# print(fruits)

# Change value
fruits[0] = 'blueberries'
print(fruits)
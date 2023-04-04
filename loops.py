"""
A loop is used for iterating over a sequence 
"""

people = ['John','Paul','george','Ringo']

# simple for loop 
# for person in people:
#     print(f'Current person: {person}')

# Break 
# for person in people:
#     if person =='george':
#         break
#     print(f'Current person: {person}')

# continue 
# for person in people:
#     if person =='george':
#         continue
#     print(f'Current person: {person}')


# range 
# for i in range(len(people)):
#     print(people[i])

# for i in range(0,11):
#     print(f'Number: {i}')

"""
While loops execute a set of statements as long as a condition is true
"""

count = 0 
while count <= 10:
    print(f'Count: {count}')
    count += 1 
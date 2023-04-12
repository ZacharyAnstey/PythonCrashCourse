# Json is commonly used with data APIS 

import json 

# sample JSON 
userJSON = '{"First_name": "Zachary", "last_name":"Anstey","Age": 25}'

# parse to dict 
user = json.loads(userJSON)
# print(user)
# print(user['First_name'])

# Dict to JSON
car = {'make': 'Ford','model':'mustang','year': 1970}
carJSON = json.dumps(car)
print(carJSON)
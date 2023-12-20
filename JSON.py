import json
import os

x = '{ "name":"John", "age":30, "city":"New York"}'
os.system('cls')
data = json.loads(x)
print(type(data)) #string to json

print(json.dumps(data)) #json to string
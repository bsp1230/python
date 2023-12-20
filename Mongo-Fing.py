import os
import Mongo
import pymongo

os.system('cls')
mongodb = Mongo.myclient
mydb = mongodb.get_database('test')
mycol = mydb.get_collection('test')

data = [{ "name": "John"}]
x = mycol.insert_many(data)
y = mycol.find_one()
print(y)
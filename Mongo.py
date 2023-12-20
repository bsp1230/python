import pymongo
import os

os.system('cls')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
#mycol = mydb["scores"]
collist = mydb.list_collection_names()
mylist = [{ "name": "John"}
]

# x = mycol.insert_many(mylist)
# y = mycol.find_one()

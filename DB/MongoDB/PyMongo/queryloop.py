import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newdatabase"]
mycol = mydb["customers"]

#address greater than S:

myquery = { "address": {"$gt": "S"} }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)




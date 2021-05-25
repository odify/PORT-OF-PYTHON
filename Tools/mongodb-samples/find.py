import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newdatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)





#import pymongo
#
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["newdatabase"]
#mycol = mydb["customers"]
#
#for x in mycol.find({},{ "address": 0 }):
#  print(x)

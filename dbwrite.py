from pymongo import MongoClient
client=MongoClient('127.0.0.1',27017)
db=client['kits']
c=db['ml']
#we have to insert the data into the ml
k=input("enter the msg:")
dummy={'msg':k}
#inserting only one document
c.insert_one(dummy)

for i in c.find():
	pass
else:
	print(i)
#for only msg
for i in c.find():
	pass
else:
	print(i['msg'])

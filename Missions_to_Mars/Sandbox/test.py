import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_collection


  
emp_rec1 = { 
        "name":"Mr.Geek2", 
        "eid":24, 
        "location":"delhi"
        } 
emp_rec2 = { 
        "name":"Mr.Shaurya2", 
        "eid":14, 
        "location":"delhi"
        } 
  
# Insert Data 
rec_id1 = collection.insert_one(emp_rec1) 
rec_id2 = collection.insert_one(emp_rec2) 
  
print("Data inserted with record ids",rec_id1," ",rec_id2) 
  
# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
    print(record) 

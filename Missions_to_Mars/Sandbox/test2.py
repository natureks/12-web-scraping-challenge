import pymongo
import scrape_mars

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_collection


  
hemisphere_image_dict = scrape_mars.scrape(2)
print(hemisphere_image_dict)


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_collection

rec_id = collection.insert_one(hemisphere_image_dict) 


  
print("Data inserted with record ids",rec_id) 
  
# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
    print(record) 

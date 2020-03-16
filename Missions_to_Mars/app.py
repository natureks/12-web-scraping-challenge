import scrape_mars as sm
from flask import Flask, redirect, jsonify, render_template
import socket

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
@app.route("/home")
@app.route("/index")
def welcome(): 
    collection = sm.connect_to_mongo()
    image_dict = sm.from_mongodb(collection, "Images", pickling=True)
    weather_dict = sm.from_mongodb(collection, "Weather", pickling=True)
    mars_facts_dict = sm.from_mongodb(collection, "Mars_Facts", pickling=True)
    
    
    image_list = []
    for key, value in image_dict.items():
        image_list.append((key, value))
    num_images = len(image_list)
    return render_template("index.html", num_images=num_images, image_list=image_list, weather_dict=weather_dict, mars_facts_dict=mars_facts_dict)

@app.route("/clear")
def db_clear():
    sm.clear_mongo_collection()
    return welcome()

@app.route("/scrape")
def invoke_scrape():
    # sm.clear_mongo_collection()
    collection = sm.connect_to_mongo()
    
    image_dict = sm.scrape_imagedata(4)
    # sm.insert_mongo('Images', image_dict)
    sm.to_mongodb(image_dict, collection, "Images", pickling=True)

    weather_dict = sm.scrape_weatherdata()
    # sm.insert_mongo('Weather', weather_dict)
    sm.to_mongodb(weather_dict, collection, "Weather", pickling=True)
    
    mars_facts_dict = sm.scrape_mars_details()
    # sm.insert_mongo('Mars_facts', mars_facts_dict)
    sm.to_mongodb(mars_facts_dict, collection, "Mars_Facts", pickling=True)

    return welcome()

@app.route("/redirect")
def redirect():

    return welcome()

@app.route("/get")
def get():
	hostname = socket.gethostname()    
	IPAddr = socket.gethostbyname(hostname)    
	print("Your Computer Name is:" + hostname)    
	print("Your Computer IP Address is:" + IPAddr)    
	ipDetails = f"Flask application IP Deails are:\nhostname='{hostname}', IPAddr='{IPAddr}'"

	return jsonify(ipDetails)
    
if __name__ == '__main__':
    app.run(debug=False)

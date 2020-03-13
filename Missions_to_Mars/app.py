import scrape_mars
from flask import Flask, jsonify
import pymongo

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/scrape")
def invoke_scrape():
    hemisphere_image_dict = scrape_mars.scrape()

    hemisphere_image_urls = []
    for key, value in hemisphere_image_dict.items():
        hemisphere_image_urls.append(f"'title':'{value}', '{key}': ''...''")
    hemisphere_image_urls

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_collection

    rec_ids = []
    for hemi in hemisphere_image_dict:
        hemisphere_image_urls.append(f"'title':'{value}', '{key}': ''...''")
        rec_id = collection.insert_one(hemi) 
        rec_ids.append(rec_id)


    return jsonify("Success")

@app.route("/dbtest")
def dbtest():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_collection

    return jsonify("Success")



if __name__ == '__main__':
    app.run(debug=False)

import scrape_mars as sm

sm.clear_mongo_collection()

weather_dict = sm.scrape_weatherdata()
sm.insert_mongo('Images', weather_dict)

mars_facts_dict = sm.scrape_mars_details()
sm.insert_mongo('Images', mars_facts_dict)
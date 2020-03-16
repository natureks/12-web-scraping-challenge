import scrape_mars as sm

sm.clear_mongo_collection()

# mars_facts_dict = sm.scrape_mars_details()
# sm.insert_mongo('Images', mars_facts_dict)

mars_facts_dict=sm.get_value_from_mongo("Images")
print("Mars Facts Type:", type(mars_facts_dict))
print(mars_facts_dict)

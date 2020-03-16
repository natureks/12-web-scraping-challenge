import scrape_mars as sm


hemisphere_image_dict = sm.scrape(2)
sm.insert_mongo(hemisphere_image_dict)

#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from pprint import pprint 
import pandas as pd
import time

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

hemisphere_image_dict = {}
def get_image_details(click_count):
    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)
    time.sleep(5)
    links = browser.find_link_by_partial_text('Hemisphere Enhanced')
    links[click_count].click()
    title = browser.find_by_css('.title').first.text
    url = browser.find_by_text('Sample').first["href"]
    hemisphere_image_dict[url] = title

for i in range(4):
    get_image_details(i)

print("Dictionary containing Hemisphere Image:")
print(hemisphere_image_dict)


hemisphere_image_urls = []
for key, value in hemisphere_image_dict.items():
    hemisphere_image_urls.append(f"'title':'{value}', '{key}': ''...''")

print("List containing Hemisphere Image:")
print(hemisphere_image_urls)



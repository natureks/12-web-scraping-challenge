#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
import time

hemisphere_image_dict = {}
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape(range_max):
    print("scrape invoked")
    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)
    time.sleep(5)
    for i in range(range_max):
        get_image_details(i)
        
    return hemisphere_image_dict

def get_image_details(click_count):
    links = browser.find_link_by_partial_text('Hemisphere Enhanced')
    links[click_count].click()
    title = browser.find_by_css('.title').first.text
    url = browser.find_by_text('Sample').first["href"]
    hemisphere_image_dict[title] = url
    browser.back()
    print("Back to main screen")

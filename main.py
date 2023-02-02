from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
import sys
import urllib3

class Restaurant:
    def __init__(self, name, link):
        self.name = name
        self.link = link

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

suburb = input("Enter your suburb: ")

driver.get('https://ubereats.com/')

location = driver.find_element("id", "location-typeahead-home-input")
location.send_keys(suburb)

sleep(2)

location.send_keys(Keys.ENTER)

sleep(3)
print("shidma")
pickupbutton = driver.find_element(By.XPATH, "//div[text()='Pickup']")
pickupbutton.click()

sleep(2)

restaurants = driver.find_elements(By.TAG_NAME, "h3")
restaurant_list = []

for restaurant in restaurants:
    link = restaurant.find_element(By.XPATH, "./..")
    restaurant_list.append(Restaurant(restaurant.text, link.get_attribute("href")))

for res in restaurant_list:
    print(res.name)
    print(res.link)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.bbc.com/sport/football"
path = "/home/anas/Downloads/chromedriver"

service = Service(excecutable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
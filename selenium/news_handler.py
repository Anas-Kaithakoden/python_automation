from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.skysports.com/football"
path = "/home/anas/Downloads/chromedriver-linux64/chromedriver"

#headless mode
options = Options()
options.add_argument("--headless=new")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)


results = driver.find_elements(by="xpath", value='//a[@class="sdc-site-tile__headline-link"]') # get the container

titles = []


for result in results: #store each data
    title = result.find_element(by="xpath", value='//a[@class="sdc-site-tile__headline-link"]').get_attribute("href")
    titles.append(title)
   
my_dict = {'title': titles}
headlines = pd.DataFrame(my_dict)
headlines.to_csv('headline_headless.csv')

driver.quit()

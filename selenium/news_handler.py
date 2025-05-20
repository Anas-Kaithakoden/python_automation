from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

if getattr(sys, 'frozen', False):
    app_path  = os.path.dirname(sys.executable) # .exe
else:
    app_path = os.path.dirname(os.path.abspath(__file__)) # .py file

now = datetime.now() # get date
month_day_year = now.strftime("%m%d%y") # change date to string 

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
    title = result.get_attribute("href")
    titles.append(title)
   
my_dict = {'title': titles}
headlines = pd.DataFrame(my_dict)

result_file = os.path.join(app_path, f'headline-{month_day_year}.csv') # concatenate 2 paths together
headlines.to_csv(result_file)

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

website = "https://books.toscrape.com/"
path = "/home/anas/Downloads/chromedriver-linux64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

driver.find_element(By.XPATH, "//ul[@class= 'nav nav-list']/li/ul/li[21]/a").click() #selects science

results_count = int(driver.find_element(By.XPATH, "//form[@class='form-horizontal']/strong").text)

elements = driver.find_elements(By.XPATH, "//div[@class='image_container']/a")
urls =[link.get_attribute('href') for link in elements]

books = []

for url in urls:
    driver.get(url)# enter into each book
    time.sleep(1) 

    name_of_book = driver.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1").text
    price_of_book =  driver.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/p[1]").text
    stock = driver.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/p[2]").text.split("(")[1].replace(")", "")

    book_data = {
        "name": name_of_book, 
        "price": price_of_book, 
        "stock": stock,
    }
    books.append(book_data)

df = pd.DataFrame(books)
df.to_csv("books.csv", index=False)
print(df)
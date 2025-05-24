from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

website = "https://orteil.dashnet.org/cookieclicker/"
path = "/home/anas/Downloads/chromedriver-linux64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

#select a language
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='langSelect-EN']"))
)
driver.find_element(By.XPATH, "//div[@id='langSelect-EN']").click()

#click cookie
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)
cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()

time.sleep(10)

product_prefix = "productPrice"
product = "product"

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    #helper
    for i in range(4):
        price = driver.find_element(By.ID, product_prefix + str(i)).text
        price = int(price.replace(",", ""))
        if cookies_count >= price:
            driver.find_element(By.ID, product + str(i)).click()






time.sleep(10)
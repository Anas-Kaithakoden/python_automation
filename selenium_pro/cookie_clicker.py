import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

website = "https://orteil.dashnet.org/cookieclicker/"
path = "/home/anas/Downloads/chromedriver-linux64/chromedriver"

#undetected chrome driver
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = uc.Chrome(options=options)

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
    print(f"cookies count: {cookies_count}")
    #helper
    for i in range(4):
        price = driver.find_element(By.ID, product_prefix + str(i)).text
        print(f"price: {price}")
        if not price:
            continue
        price = int(price.replace(",", ""))  
        if cookies_count >= price:
            driver.find_element(By.ID, product + str(i)).click()
            print(f"Helper {i} brought")
        else:
            continue




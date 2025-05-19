from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "/home/anas/Downloads/chromedriver"

service = Service(excecutable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)


results = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for result in results:
    title = result.find_element(by="xpath", value='./a/span').text
    titles.append(title)

    subtitle = result.find_element(by="xpath", value='./a/h3').text
    subtitles.append(subtitle)

    link = result.find_element(by="xpath", value='/a').get_attribute("href")
    links.append[link]



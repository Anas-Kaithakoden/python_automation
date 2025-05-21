import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import re

content = ''



def extract_news():
    print("Extrating news...")
    cnt = ''

    response = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in (soup.find_all('td',attrs={'class':'title'})):
        text = tag.text.strip()
        if not re.match(r'^\d+\.', text) and text.lower() != "more":
            cnt += tag.text + "\n"


    return cnt

data = extract_news()
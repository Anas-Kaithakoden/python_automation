import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import re
import os


content = ''

def extract_news(url):
    print("Extrating news...")
    cnt = '<b>HN Top stories: </b><br>'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in (soup.find_all('td',attrs={'class':'title'})):
        text = tag.text.strip()
        if not re.match(r'^\d+\.', text) and text.lower() != "more":
            cnt += tag.text + "<br>"

    return cnt

data = extract_news("https://news.ycombinator.com/")
content += data + ('<br><br>End of the Message')

print('Composing Email...')

# Email parameters
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.environ.get("MY_EMAIL")
TO = os.environ.get("SEND_EMAIL")
PASS = os.environ.get("MY_PASSWORD")

msg = MIMEMultipart()

# Email body
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' '  + str(datetime.now().day) + ' ' + str(datetime.now().month) + ' ' + str(datetime.now().year)
msg['from'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

# Authenticating
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo() #initiate
server.starttls() #start a TLS connection
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email send...')

server.quit()
import requests
from bs4 import BeautifulSoup
import smtplib

def check_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])
    print(title.strip())
    print(converted_price)

    if(converted_price<170.0):
        send_mail(url)

def send_mail(url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('drsamypal@gmail.com', 'mupmsslpsuuxubhc')
    subject = 'Price Down - From my App'
    body = f'Check the amazon link: {url}'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'drsamypal@gmail.com',
        'ram.cecri@gmail.com',
        msg
    )

    print('Email Sent!!')
    server.quit()


url = 'https://www.amazon.de/Samsung-Galaxy-Active-Smartwatch-dunkelgrau/dp/B07NK49QP1/ref=sr_1_3?dchild=1&keywords=samsung+galaxy+active+watch+2&qid=1588127941&refinements=p_89%3ASamsung&rnid=669059031&sr=8-3'
check_price(url)

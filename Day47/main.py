import requests
from bs4 import BeautifulSoup
import smtplib

url = input("Enter the URL of the product you want to track:\n")
price_alert = int(input("enter ammount below which you want alert:\n"))

MY_EMAIL = "Your_email_id"
MY_PASSWORD = "Your_app_password"

# Goto http://myhttpheader.com/ and copy and add the respective parameter values.
header = {
    "User-Agent": "",
    "Accept-Language": ""
}

response = requests.get(url=url,headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
current_price = soup.select_one(".a-price-whole")
product_title = soup.select("#productTitle")[0].getText().strip()
first_half = current_price.getText().split(',')[0]
second_half = current_price.getText().split(',')[1].split('.')[0]
price = int(f"{first_half}{second_half}")

if price < price_alert: 
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:New Price Drop Alert!\n\nThe Price for the {product_title} has dropped to {price}. Click below to buy.\n{url}".encode('utf-8')
        )


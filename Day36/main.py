import requests
from twilio.rest import Client

# Your Desired Stock Details
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "Your Twilio Account SID"
auth_token = "Your Twilio Account auth token"

STOCK_PARAMETERS = {
    "apikey": "API key",  # Your API key from https://www.alphavantage.co/
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
}

NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "apiKey": "API Key",  # Your API key from https://newsapi.org/
    "searchIn": "title"
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data = [value for (key, value) in data.items()]
yesterday_closing = float(data[0]["4. close"])
day_before_yesterday_closing = float(data[1]["4. close"])
change_in_price = round(((yesterday_closing-day_before_yesterday_closing)/yesterday_closing)*100, 2)
print(change_in_price)
if change_in_price >= 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(change_in_price) >= 0.5:
    print("Get News")
    response = requests.get(url=NEWS_ENDPOINT,params=NEWS_PARAMETERS)
    response.raise_for_status()
    news_articles = response.json()['articles'][:3]
    print(news_articles)
    client = Client(account_sid, auth_token)
    for article in news_articles:
        message = client.messages.create(
          from_='mobile number you got from twilio',
          body=f"{STOCK}: {up_down}{change_in_price}% Headline: {article['title']}\nBrief: {article['description']}",
          to='your mobile number'
        )

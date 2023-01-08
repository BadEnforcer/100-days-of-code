import os
from datetime import datetime
from twilio.rest import Client
import requests

time_now = datetime.now()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_exchange_endpoint = "https://www.alphavantage.co/query"
stock_exchange_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "qInTitle": f"{COMPANY_NAME}",
    "apikey": os.environ["STOCK_DATA_API_KEY"]
}


def get_stock_data():
    website_response = requests.get(url=stock_exchange_endpoint, params=stock_exchange_params)
    website_response.raise_for_status()
    stock_raw_data = website_response.json()["Time Series (Daily)"]
    # print(stock_raw_data)
    day_keys = list(stock_raw_data.keys())[:2]
    yesterday = float((stock_raw_data[day_keys[0]]['4. close']))
    price_difference = float((stock_raw_data[day_keys[0]]['4. close'])) - float(stock_raw_data[day_keys[1]]['4. close'])

    if (abs(price_difference / yesterday) * 100) < 5:
        exit("no need to send msg")

    if price_difference < 0:
        is_growing = False
    else:
        is_growing = True

    return {"direction": is_growing,
            "percentage": round((abs(price_difference) / yesterday) * 100, 2)}


# STEP 2: Use https://newsapi.org
news_url = "https://newsapi.org/v2/everything"
news_params = {"q": COMPANY_NAME,
               "apikey": os.environ["NEWS_API_KEY"],
               "from_param": f'{time_now.year}-01-01',
               "language": 'en',
               "page_Size": 3,
               "sort_by": 'publishedAt'
               }


def get_news():
    news_response = requests.get(url=news_url, params=news_params)
    news_response.raise_for_status()
    news_database = news_response.json()["articles"]
    news = {}
    for article in news_database[:3]:
        news[article["title"]] = article['description']
    return news


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:

def send_message():
    # twilio setup

    client = Client(account_sid, auth_token)

    # get details
    news_details = get_news()
    news_keys = list(news_details.keys())
    news_content = ""
    for n in range(0, 3):
        news_content += f"News: {n + 1}\n" \
                        f"Headline: {news_keys[n]}\n" \
                        f"Brief: {news_details[news_keys[n]]}\n"

    print(news_content)
    message_type = get_stock_data()
    if message_type["direction"]:
        message = client.messages.create(to="+917905179829",
                                         from_="+18145616566",
                                         body=f"{STOCK}: 🔺{message_type['percentage']}%\n"
                                              f"{news_content}")

        print(message.status)
    else:
        message = client.messages.create(to="+917905179829",
                                         from_="+18145616566",
                                         body=f"{STOCK}: 🔻{message_type['percentage']}%\n"
                                              f"{news_content}")

        print(message.status)


send_message()
"""

Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

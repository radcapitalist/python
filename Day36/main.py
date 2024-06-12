
import requests
from dotenv import load_dotenv
import os
from newsapi import NewsApiClient

load_dotenv()

STOCK = "GME"
COMPANY_NAME = "GameStop"
PRICE_API_KEY = os.environ.get("ALPHA_VANTAGE_KEY")
NEWS_API_KEY = os.environ.get("NEWS_KEY")
PCT_CHANGE_TRIGGER = 2.0

news_obj = NewsApiClient(api_key=NEWS_API_KEY)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={PRICE_API_KEY}&outputsize=compact'
r = requests.get(url)
data:dict = r.json()
ts_data:dict = data["Time Series (Daily)"]
dates:list = list(ts_data.keys())
max_index = min(len(dates) - 2, 20)
get_news = False
for index in range(0, max_index):
    curr_day = ts_data[dates[index]]
    curr_close = float(curr_day["4. close"])
    prev_day = ts_data[dates[index + 1]]
    prev_close = float(prev_day["4. close"])
    pct_change = ((curr_close - prev_close) / prev_close) * 100
    print(f'Date: {dates[index]}  Close: {curr_close}  Prev Close: {prev_close}  Pct Change: {"{0:.2f}".format(pct_change)} %')
    # If price change is more than + or - PCT_CHANGE_TRIGGER percent on any day in the range, get news
    if pct_change >= PCT_CHANGE_TRIGGER or pct_change < -PCT_CHANGE_TRIGGER:
        get_news = True

## STEP 2: Use https://newsapi.org
if get_news:
    result = news_obj.get_top_headlines(q=COMPANY_NAME, page_size=3)
    print(result)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


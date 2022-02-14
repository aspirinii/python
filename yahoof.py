import yfinance as yf
import datetime
ticker = ['GOOGL', "TSLA"]
# for j in range(1,10) :
#     for i in ticker :
#         stock = yf.Ticker(i)
#         currentTime = datetime.datetime.now()
#         # get stock info
#         currentPrice = stock.info['currentPrice']
#         print(j," try")
#         print(f"{i} currentPrice : {currentPrice}")
#         print(f"{i} currentTime : {currentTime}")


msft = yf.Ticker("BA")
msft.info['currentPrice']

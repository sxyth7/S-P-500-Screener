import numpy as np
import pandas as pd 
import requests #considered the gold standard for making http requests you can send to an api to get back some data, Using this to make api calls 
import xlsxwriter # lets you create Excel files (.xlsx) from your Python code
import math
import yfinance as yf
import matplotlib.pyplot as plt
stocks = pd.read_csv('sp_500_stocks.csv')
tickers = stocks['Ticker'].tolist() #From that table, grab just the Ticker column (AAPL, GOOGL, TSLA...) and convert it into a simple Python list
data = yf.download(tickers, period = "1d", auto_adjust = True)
#yf.download → go to Yahoo Finance and download something
#tickers → download data for these 500 stocks
#period="1d" → only get today's data (1 day)
#auto_adjust=True → make sure prices are accurate (adjusts for stock splits etc, don't worry about this for now)
#data = → store everything you downloaded in a variable called data**
prices = data['Close'].iloc[-1]
#print(prices)
#Ticker
#AAPL     189.50
#ABBV     145.23
#ABNB      98.12
#ABT       87.45
#CGL      67.23
#ADBE     234.12
#ADI      156.78
#ADM       45.67
#ADP      198.34
#ADSK     167.89
#..
#(500 rows total)
portfolio_size = float(input("Enter the value of your portfolio in USD: "))
position_size = portfolio_size/500
results = []
for ticker in tickers:
    if ticker in prices and not pd.isna(prices[ticker]):
        price = prices[ticker]
        shares = math.floor(position_size/price)
        results.append([ticker,price,shares,position_size])
df = pd.DataFrame(results, columns =["Ticker","Prices","Shares to buy","Allocation"])
print(df)
df_sorted = df.sort_values('Shares to buy', ascending=False).head(20)

plt.figure(figsize=(14, 7))
plt.bar(df_sorted['Ticker'], df_sorted['Shares to buy'], color='steelblue')
plt.title('Top 20 Stocks by Shares to Buy')
plt.xlabel('Ticker')
plt.ylabel('Shares to Buy')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




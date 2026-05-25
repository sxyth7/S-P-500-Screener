import streamlit as st
import pandas as pd
import yfinance as yf
import math
import matplotlib.pyplot as plt

st.title('S&P 500 SCREENER')

portfolio_size = st.number_input('Enter your portfolio size in USD', min_value=1000, value=10000)

if st.button('Calculate'):
    with st.spinner('Fetching stock data...'):
        stocks = pd.read_csv('sp_500_stocks.csv')
        tickers = stocks['Ticker'].tolist()
        data = yf.download(tickers, period="1d", auto_adjust=True)
        prices = data['Close'].iloc[-1]

        position_size = portfolio_size / 500
        results = []
        for ticker in tickers:
            if ticker in prices and not pd.isna(prices[ticker]):
                price = prices[ticker]
                shares = math.floor(position_size / price)
                results.append([ticker, price, shares, position_size])

        df = pd.DataFrame(results, columns=["Ticker", "Price", "Shares to Buy", "Allocation"])

        st.dataframe(df)

        df_sorted = df.sort_values('Shares to Buy', ascending=False).head(20)
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.bar(df_sorted['Ticker'], df_sorted['Shares to Buy'], color='steelblue')
        ax.set_title('Top 20 Stocks by Shares to Buy')
        ax.set_xlabel('Ticker')
        ax.set_ylabel('Shares to Buy')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
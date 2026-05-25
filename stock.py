import yfinance as yf
import matplotlib.pyplot as plt

TICKER = "AAPL"
PERIOD = "1y"

df = yf.download(TICKER, period=PERIOD)

df["MA50"]  = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()

plt.figure(figsize=(14, 7))
plt.plot(df["Close"], label="Close Price", color="black", linewidth=1.2)
plt.plot(df["MA50"],  label="50-day MA",   color="orange", linewidth=1.5)
plt.plot(df["MA200"], label="200-day MA",  color="cyan",   linewidth=1.5)
plt.legend()
plt.title("AAPL Stock Price")
plt.show()
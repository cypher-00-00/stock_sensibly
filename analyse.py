import yfinance as yf

df = yf.download("TSLA",period="1y",interval="1d")

df["Average"] = df["Close"].rolling(window=10).mean()
df["Return"] = df["Close"].pct_change()

print(df[["Close","Average", "Return"]].tail(10))
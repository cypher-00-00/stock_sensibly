import yfinance as yf

df=yf.download("TSLA",period="6mo",interval="1d")
print(df.head())
print(df.tail())
print(df.shape)
print(df['Close'])
print(df['Close'].max())
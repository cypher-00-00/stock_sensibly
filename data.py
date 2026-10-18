import yfinance as yf

def get_data(ticker, period="1y"):
    df = yf.download(ticker, period=period, interval="1d",
                     auto_adjust=True, multi_level_index=False)
    return df
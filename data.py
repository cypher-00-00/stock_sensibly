from datetime import date, timedelta
import yfinance as yf
from db import save_prices, load_prices

def get_data(ticker):
    df = load_prices(ticker)
    stale = df.empty or df.index.max().date() < date.today() - timedelta(days=1)

    if stale:
        fresh = yf.download(ticker, period="5y", interval="1d",
                            auto_adjust=True, multi_level_index=False)
        if not fresh.empty:
            save_prices(ticker, fresh)
            df = load_prices(ticker)
    return df
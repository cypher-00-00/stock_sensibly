def add_indicators(df):
    df = df.copy()
    df["avg_20"] = df["Close"].rolling(20).mean()
    df["avg_50"] = df["Close"].rolling(50).mean()
    df["return"] = df["Close"].pct_change()
    df["volatility"] = df["return"].rolling(20).std()
    return df
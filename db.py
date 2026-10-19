import sqlite3
import pandas as pd

DB_PATH = "stocksense.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            ticker TEXT, date TEXT,
            open REAL, high REAL, low REAL, close REAL, volume INTEGER,
            PRIMARY KEY (ticker, date)
        )""")
    return conn

def save_prices(ticker, df):
    rows = [(ticker, d.strftime("%Y-%m-%d"), r.Open, r.High, r.Low, r.Close, int(r.Volume))
            for d, r in df.iterrows()]
    with get_conn() as conn:
        conn.executemany("INSERT OR REPLACE INTO prices VALUES (?,?,?,?,?,?,?)", rows)

def load_prices(ticker):
    query = """SELECT date, open AS Open, high AS High, low AS Low,
                      close AS Close, volume AS Volume
               FROM prices WHERE ticker = ? ORDER BY date"""
    with get_conn() as conn:
        df = pd.read_sql(query, conn, params=(ticker,),
                         parse_dates=["date"], index_col="date")
    df.index.name = "Date"
    return df
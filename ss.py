import streamlit as sl
import plotly.graph_objects as go
from data import get_data
from anal import add_indicators

sl.title("StockSense")

ticker = sl.text_input("Ticker","AAPL").upper()
period = sl.selectbox("Period",["1mo","3mo","6mo","1y","2y","5y"],index=3)

df = get_data(ticker,period)

if df.empty:
    sl.error("No data found lol.")
else:
    df = add_indicators(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name="Close"))
    fig.add_trace(go.Scatter(x=df.index, y=df["avg_20"], name="Average:20 Days"))
    fig.add_trace(go.Scatter(x=df.index, y=df["avg_50"], name="Average:50 Days"))
    fig.add_trace(go.Scatter(x=df.index, y=df["Return"], name="Return"))
    fig.update_layout(title=f"{ticker} price", xaxis_title="Date", yaxis_title="Price")

    sl.plotly_chart(fig, use_container_width=True)
    sl.dataframe(df.tail(10))
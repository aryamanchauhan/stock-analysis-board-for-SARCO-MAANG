# arya_subsidiaries.py

import yfinance as yf
import pandas as pd

ticker = "2222.SR"
df_aramco = yf.download(ticker, start="2018-01-01")
df_aramco.reset_index(inplace=True)
df_aramco['Daily Return'] = df_aramco['Close'].pct_change()
df_aramco['Volatility'] = df_aramco['Daily Return'].rolling(window=30).std()
df_aramco.to_csv("aramco_data.csv", index=False)

ticker = "2380.SR"
df_petro = yf.download(ticker, start="2018-01-01")
df_petro.reset_index(inplace=True)
df_petro['Daily Return'] = df_petro['Close'].pct_change()
df_petro['Volatility'] = df_petro['Daily Return'].rolling(window=30).std()
df_petro.to_csv("petro_rabigh_data.csv", index=False)

ticker = "2010.SR"
df_sabic = yf.download(ticker, start="2018-01-01")
df_sabic.reset_index(inplace=True)
df_sabic['Daily Return'] = df_sabic['Close'].pct_change()
df_sabic['Volatility'] = df_sabic['Daily Return'].rolling(window=30).std()
df_sabic.to_csv("sabic_data.csv", index=False)

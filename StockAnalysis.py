import pandas as pd
import yfinance as yf

ticker = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

stock_data = yf.download(ticker, start=start_date, end=end_date)

stock_data['Price_Change'] = stock_data['Close'] - stock_data['Open']

print(stock_data.head())

import pandas as pd
import yfinance as yf

# Define the ticker symbol and timeframe
ticker = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

# Retrieve stock price data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Calculate daily price change
stock_data['Price_Change'] = stock_data['Close'] - stock_data['Open']

# Display the first few rows of the data
print(stock_data.head())

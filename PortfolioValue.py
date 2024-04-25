import pandas as pd

# Sample portfolio data
portfolio_data = {
    'Asset': ['AAPL', 'GOOGL', 'MSFT'],
    'Quantity': [100, 50, 75],
    'Price': [150.25, 2800.50, 250.75]
}

# Create a DataFrame from the portfolio data
portfolio_df = pd.DataFrame(portfolio_data)

# Calculate the value of each asset
portfolio_df['Value'] = portfolio_df['Quantity'] * portfolio_df['Price']

# Calculate the total portfolio value
total_portfolio_value = portfolio_df['Value'].sum()

# Display the portfolio DataFrame and total value
print(portfolio_df)
print("Total Portfolio Value:", total_portfolio_value)

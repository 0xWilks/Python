import pandas as pd

portfolio_data = {
    'Asset': ['AAPL', 'GOOGL', 'MSFT'],
    'Quantity': [100, 50, 75],
    'Price': [150.25, 2800.50, 250.75]
}

portfolio_df = pd.DataFrame(portfolio_data)

portfolio_df['Value'] = portfolio_df['Quantity'] * portfolio_df['Price']

total_portfolio_value = portfolio_df['Value'].sum()

print(portfolio_df)
print("Total Portfolio Value:", total_portfolio_value)

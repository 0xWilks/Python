import numpy as np

# Sample portfolio returns
portfolio_returns = [0.02, 0.03, -0.01, 0.05, 0.04]

# Calculate average return
average_return = np.mean(portfolio_returns)

# Calculate standard deviation of return (risk)
risk = np.std(portfolio_returns)

# Calculate Sharpe ratio
sharpe_ratio = average_return / risk

# Display performance metrics
print("Average Return:", average_return)
print("Risk (Standard Deviation):", risk)
print("Sharpe Ratio:", sharpe_ratio)

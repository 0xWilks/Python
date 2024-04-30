import numpy as np

portfolio_returns = [0.02, 0.03, -0.01, 0.05, 0.04]

average_return = np.mean(portfolio_returns)

risk = np.std(portfolio_returns)

sharpe_ratio = average_return / risk

print("Average Return:", average_return)
print("Risk (Standard Deviation):", risk)
print("Sharpe Ratio:", sharpe_ratio)

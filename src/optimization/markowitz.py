from scipy.optimize import minimize
import numpy as np
import pandas as pd

#We want to minimize the portfolio's negative sharpe ratio
def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return -(portfolio_return - risk_free_rate) / portfolio_std_dev

def optimize_portfolio(mean_returns, cov_matrix, tickers, risk_free_rate=0.01):
    num_assets = len(mean_returns)
    initial_guess = num_assets * [1. / num_assets]  # start with equal weights
    bounds = tuple((0, 1) for _ in range(num_assets))  # no shorting
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # weights sum to 1

    result = minimize(
        neg_sharpe_ratio,
        initial_guess,
        args=(mean_returns, cov_matrix, risk_free_rate),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    # Convert to DataFrame
    optimal_weights = pd.DataFrame(
        data=[result.x],
        columns=tickers,
        index=["Weight"]
    ).T

    # Format as percentages
    optimal_weights.columns = ["Weight (%)"]
    optimal_weights["Weight (%)"] = optimal_weights["Weight (%)"] * 100

    return optimal_weights.round(2)


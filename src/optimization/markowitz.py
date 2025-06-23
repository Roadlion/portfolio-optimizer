from scipy.optimize import minimize
import numpy as np
import pandas as pd

#We want to minimize the portfolio's negative sharpe ratio

def optimize_portfolio(mean_returns, cov_matrix, risk_free_rate, trading_days):

    num_assets = len(mean_returns) #Number of assets (duh)

    #initial guess
    init_guess =np.array(num_assets * [1. /num_assets])

    # Constraints: weights must sum to 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})

    # Bounds: weights between 0 and 1 (no short selling)
    bounds = tuple((0, 1) for _ in range(num_assets))   

     # Objective function: Negative Sharpe Ratio
    def neg_sharpe_ratio(weights):
        portfolio_return = np.dot(weights, mean_returns) * trading_days
        portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(trading_days)
        sharpe = (portfolio_return - risk_free_rate) / portfolio_vol
        return -sharpe  # Because we want to maximize Sharpe

    # Run optimization
    result = minimize(neg_sharpe_ratio, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)

    if not result.success:
        raise BaseException("Optimization failed: " + result.message)

    # Return weights as pd.Series with asset names
    optimized_weights = pd.Series(result.x, index=mean_returns.index)
    return optimized_weights

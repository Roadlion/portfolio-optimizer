import numpy as np
import pandas as pd

def calculate_daily_returns(prices: pd.DataFrame, use_log: bool = False) -> pd.DataFrame:
    #Can use log returns or simple returns. Use log returns for portfolio optimization
    if use_log:
        return np.log(prices / prices.shift(1)).dropna()
    else:
        return prices.pct_change().dropna()

def calculate_mean_returns(daily_returns):
    return daily_returns.mean()

def annualize_returns(mean_returns, trading_days):
    return mean_returns * trading_days

def calculate_covariance_matrix(daily_returns):
    return daily_returns.cov()
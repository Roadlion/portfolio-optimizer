import pandas as pd
import numpy as np
from typing import Tuple
import statsmodels.api as sm
from typing import Tuple, Union

def calculate_excess_returns(returns: pd.Series, risk_free_rate: float) -> pd.Series:
    """
    Calculates excess returns of an asset over the risk-free rate.
    """
    return returns - risk_free_rate

def run_capm_regression(
    asset_returns: Union[pd.Series, pd.DataFrame],
    market_returns: pd.Series
) -> Union[Tuple[float, float], pd.DataFrame]:
    """
    Runs CAPM regression to estimate alpha and beta.
    
    Parameters:
        asset_returns: pd.Series or pd.DataFrame
            Daily returns of one stock (Series) or multiple stocks (DataFrame).
        market_returns: pd.Series
            Daily returns of the market index.
    
    Returns:
        If input is Series:
            (alpha, beta) tuple of floats.
        If input is DataFrame:
            pd.DataFrame with 'alpha' and 'beta' columns, index = tickers.
    """
    
    def single_regression(stock_returns: pd.Series) -> Tuple[float, float]:
        # Align data and drop missing values
        df = pd.concat([stock_returns, market_returns], axis=1).dropna()
        y = df.iloc[:, 0]
        X = sm.add_constant(df.iloc[:, 1])
        model = sm.OLS(y, X).fit()
        alpha = model.params['const']
        beta = model.params[df.columns[1]]
        return alpha, beta


    if isinstance(asset_returns, pd.Series):
        return single_regression(asset_returns)
    
    elif isinstance(asset_returns, pd.DataFrame):
        results = {'alpha': [], 'beta': []}
        for ticker in asset_returns.columns:
            alpha, beta = single_regression(asset_returns[ticker])
            results['alpha'].append(alpha)
            results['beta'].append(beta)
        return pd.DataFrame(results, index=asset_returns.columns)
    
    else:
        raise TypeError("asset_returns must be a pandas Series or DataFrame")

def calculate_expected_return_capm(
    beta: pd.Series,
    market_return,
    risk_free_rate: float
) -> pd.Series:
    """
    Calculates expected return using CAPM formula.
    Accepts a Series of betas and a Series/scalar market return.
    """
    # If market_return is a Series or DataFrame, extract its first value
    if isinstance(market_return, (pd.Series, pd.DataFrame)):
        market_return = market_return.squeeze().item()
    print("\n")
    print("Expected Returns")
    return risk_free_rate + beta * (market_return - risk_free_rate)



def get_capm_expected_return(
    asset_returns: pd.Series,
    market_returns: pd.Series,
    risk_free_rate: float,
    avg_market_return: float
) -> Tuple[float, float, float]:
    """
    Combines all CAPM steps:
    - Calculates excess returns
    - Regresses alpha and beta
    - Computes expected return using CAPM

    Returns: (alpha, beta, expected_return)
    """
    excess_asset_returns = calculate_excess_returns(asset_returns, risk_free_rate)
    excess_market_returns = calculate_excess_returns(market_returns, risk_free_rate)

    alpha, beta = run_capm_regression(excess_asset_returns, excess_market_returns)
    expected_return = calculate_expected_return_capm(beta, avg_market_return, risk_free_rate)

    return alpha, beta, expected_return

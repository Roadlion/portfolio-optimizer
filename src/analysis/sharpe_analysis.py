import numpy as np

def calc_sharpe_ratio(expected_returns, weights, cov_matrix, trading_days, risk_free_rate):
    """
    Calculates Sharpe Ratio and interprets volatility.

    Parameters:
    - mean_returns: array-like of expected returns per asset (from CAPM or historical)
    - weights: array-like of portfolio weights (should sum to 1)
    - cov_matrix: covariance matrix of asset returns
    - trading_days: number of trading days in the chosen period
    - risk_free_rate: annualized risk-free rate (default is 4.4%)

    Returns:
    - sharpe_ratio: float
    - portfolio_volatility: float (annualized %)
    """
    # Annualized portfolio return
    portfolio_return = np.dot(weights, expected_returns) * trading_days

    # Annualized volatility (percentage)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(trading_days) * 100

    # Sharpe Ratio
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    # Interpret Sharpe Ratio
    print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
    if sharpe_ratio < 1.0:
        print("Sharpe Ratio Interpretation: Poor risk-adjusted return")
    elif sharpe_ratio < 2.0:
        print("Sharpe Ratio Interpretation: Acceptable to Good")
    elif sharpe_ratio < 3.0:
        print("Sharpe Ratio Interpretation: Very good")
    else:
        print("Sharpe Ratio Interpretation: Excellent")

    # Interpret Volatility
    print(f"Portfolio Volatility: {portfolio_volatility:.2f}%")
    if portfolio_volatility < 10:
        print("Volatility Interpretation: Cash-like stability")
    elif portfolio_volatility < 15:
        print("Volatility Interpretation: Defensive")
    elif portfolio_volatility < 20:
        print("Volatility Interpretation: Typical diversified portfolio")
    elif portfolio_volatility < 30:
        print("Volatility Interpretation: Aggressive growth")
    elif portfolio_volatility < 50:
        print("Volatility Interpretation: Speculative")
    else:
        print("Volatility Interpretation: Casino-level risk")

    return sharpe_ratio, portfolio_volatility

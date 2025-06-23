import pandas as pd

def project_returns_in_dollars(weights, mean_returns, trading_days, total_investment):
    """
    Projects the expected annual returns in dollars for each stock in the portfolio.

    Parameters:
    - weights: pd.Series with tickers as index and weights as values (decimal)
    - mean_returns: pd.Series with tickers as index and expected daily returns
    - total_investment: float, the total dollar amount invested
    - trading_days: int, number of trading days in a year (default: 252)

    Returns:
    - pd.DataFrame showing weight %, dollar allocation, and expected return per stock
    """
    
    df = pd.DataFrame({
        'Weight (%)': weights * 100,
        'USD Allocation': weights * total_investment,
        'Expected Return ($)': weights * total_investment * mean_returns * trading_days
    })

    df = df.round(2)

    # Add total row
    totals = pd.DataFrame(df.sum()).T
    totals.index = ['TOTAL']
    df = pd.concat([df, totals])

    return df
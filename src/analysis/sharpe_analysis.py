import numpy as np
import pandas as pd
#Sharpe Ratio Function
def calc_sharpe_ratio(total_investment, tickers, weights, mean_returns, cov_matrix, trading_days, risk_free_rate=0.044):
    portfolio_return = np.dot(weights, mean_returns) * trading_days #np.dot used for multiplication, if array are both 2D then it does matrix multiplication. already annualized.
    
    portfolio_volatility = (np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(trading_days))*100 #percentage
    
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility #calculates Sharpe Ratio

    weights_df = pd.DataFrame(data=weights, index=tickers, columns=['Weight']) #how much weight each asset has

    weights_df['Weight'] = weights_df['Weight'] * 100  # convert to percent

    # Calculate dollar allocation per stock
    weights_df['USD Allocation'] = weights_df['Weight'] * total_investment

    # Reorder columns for clarity
    weights_df = weights_df[['Weight', 'USD Allocation']]

    weights_df['Projected Return ($)'] = portfolio_return*weights_df['USD Allocation']
    weights_df = weights_df[['Weight', 'USD Allocation', 'Projected Return ($)']]

    total_projected_return_usd = weights_df['Projected Return ($)'].sum()


    print(f"Sharpe Ratio: {sharpe_ratio:.4f}")

    
    if sharpe_ratio < 1.0:
        print("Sharpe Ratio Intepretation: Poor risk adjusted return")
    elif sharpe_ratio == 1.0:
        print("Sharpe Ratio Intepretation: Acceptable")
    elif sharpe_ratio > 1.0:
        print("Sharpe Ratio Intepretation: Good")
    elif sharpe_ratio > 2.0:
        print("Sharpe Ratio Intepretation: Very good")
    elif sharpe_ratio > 3.0:
        print("Sharpe Ratio Intepretation: Excellent")
    

    print(f"Portfolio Return: {portfolio_return:.4f}")

    print(f"Portfolio Volatility: {portfolio_volatility:.4f}%")

    if portfolio_volatility < 10:
        print("Volatility Intepretation: Cash-like stability")
    elif portfolio_volatility < 15:
        print("Volatility Intepretation: Defensive, low sensitivity to markets")
    elif portfolio_volatility < 20:
        print("Volatility Intepretation: Typical diversified portfolio")
    elif portfolio_volatility < 30:
        print("Volatility Intepretation: Aggressive growth/sector risk ")
    elif portfolio_volatility < 50:
        print("Volatility Intepretation: Speculative, large swings")
    elif portfolio_volatility > 50:
        print("Volatility Intepretation: Casino-level risk")
    
    print("Portfolio Weights (%):")
    
    print(weights_df)

    print(f"Total Projected Returns ($): {total_projected_return_usd:.2f}")
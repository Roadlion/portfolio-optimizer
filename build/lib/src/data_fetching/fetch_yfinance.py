#Start of sexy sexy YAHOOO fetcher code :P

import yfinance as yf #shortening yfinance to yf
import pandas as pd #shortening pandas to pd

#Writing the function to get price data of stocks based on their tickers and start date and end date now.
def get_price_data(tickers, start, end):
    #FETCH DATA
    data = yf.download(tickers, start=start, end=end, auto_adjust=True) #calling Yahoo Finance's download function to download our data based on tickers and date range
    return data['Close'] #returns ADJUSTED closing price
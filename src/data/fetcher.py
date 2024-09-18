import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch stock data for given tickers and date range.
    
    :param tickers: List of stock tickers
    :param start_date: Start date for data fetching (YYYY-MM-DD)
    :param end_date: End date for data fetching (YYYY-MM-DD)
    :return: DataFrame with stock prices
    """
    try:
        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
        if isinstance(data, pd.Series):
            data = data.to_frame()
        if data.empty:
            raise ValueError("No data available for the given tickers and date range.")
        return data
    except Exception as e:
        raise ValueError(f"Error fetching stock data: {str(e)}")
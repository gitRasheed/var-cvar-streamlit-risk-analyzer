import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    try:
        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
        if isinstance(data, pd.Series):
            data = data.to_frame()
        if data.empty:
            raise ValueError("No data available for the given tickers and date range.")
        return data
    except Exception as e:
        raise ValueError(f"Error fetching stock data: {str(e)}")
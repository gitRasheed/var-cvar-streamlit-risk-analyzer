import yfinance as yf
import pandas as pd


def fetch_stock_data(tickers, start_date, end_date):
    try:
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)

        if data.empty:
            raise ValueError("No data available for the given tickers and date range.")

        if "Adj Close" in data.columns:
            data = data["Adj Close"]
        elif len(data.columns.levels) > 1 and "Adj Close" in data.columns.levels[0]:
            data = data["Adj Close"]
        else:
            if "Close" in data.columns:
                data = data["Close"]
            elif len(data.columns.levels) > 1 and "Close" in data.columns.levels[0]:
                data = data["Close"]
            else:
                raise ValueError(
                    "Neither 'Adj Close' nor 'Close' columns are available in the data"
                )

        if isinstance(data, pd.Series):
            if isinstance(tickers, list) and len(tickers) == 1:
                data = data.to_frame(name=tickers[0])
            else:
                data = data.to_frame()

        return data
    except Exception as e:
        raise ValueError(f"Error fetching stock data: {str(e)}")

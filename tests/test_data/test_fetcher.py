import pytest
from src.data.fetcher import fetch_stock_data


def test_fetch_stock_data():
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    data = fetch_stock_data([ticker], start_date, end_date)

    assert not data.empty
    assert "Adj Close" in data.columns
    assert data.index[0].strftime("%Y-%m-%d") >= start_date
    assert data.index[-1].strftime("%Y-%m-%d") <= end_date


def test_fetch_stock_data_single_ticker_column():
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    data = fetch_stock_data([ticker], start_date, end_date)

    assert not data.empty
    assert data.columns[0] == "Adj Close"
    assert data.index[0].strftime("%Y-%m-%d") >= start_date
    assert data.index[-1].strftime("%Y-%m-%d") <= end_date


def test_fetch_stock_data_multiple_stocks():
    tickers = ["AAPL", "GOOGL", "MSFT"]
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    data = fetch_stock_data(tickers, start_date, end_date)

    assert not data.empty
    assert all(ticker in data.columns for ticker in tickers)
    assert data.index[0].strftime("%Y-%m-%d") >= start_date
    assert data.index[-1].strftime("%Y-%m-%d") <= end_date


def test_fetch_stock_data_invalid_ticker():
    ticker = "INVALID_TICKER"
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    with pytest.raises(ValueError):
        fetch_stock_data([ticker], start_date, end_date)

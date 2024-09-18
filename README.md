# 📊 VaR and CVaR Calculator: Financial Risk Analysis Tool

## Overview

This Streamlit web app calculates and visualizes Value at Risk (VaR) and Conditional Value at Risk (CVaR) for custom stock portfolios.

## Features

- **Custom Portfolio Creation**: Input any publicly traded stock tickers and weights
- **Multiple Calculation Methods**: Historical, Parametric, and Monte Carlo simulations
- **Adjustable Parameters**: Confidence level, time horizon, and date range
- **Interactive Visualizations**: Distribution histograms and rolling window plots
- **Real-time Data**: Utilizes yfinance for up-to-date market information

## Modules Used

- 🛠️ **Framework**: Streamlit for rapid development and deployment
- 🐼 **Data Handling**: Pandas for efficient data manipulation
- 💹 **Financial Data**: yfinance for retrieving historical stock data
- 📊 **Visualizations**: Plotly for interactive, publication-quality graphs
- 🧪 **Statistical Computations**: NumPy and SciPy for robust calculations
- ✅ **Code Quality**: Pytest for unit testing, ensuring reliability and maintainability

## Installation and Usage

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run streamlit_app.py`

## Future Enhancements

- Portfolio Stress Testing: Simulate performance under historical crisis scenarios (e.g., 2008 Financial Crisis, 2020 Pandemic, Dot-com Bubble)

## Acknowledgements

Inspiration for this project came from Prudhvi Reddy's implementation of a similar web application. Their work provided valuable insights into the practical application of financial risk metrics in a web environment.

[LinkedIn](https://www.linkedin.com/in/khoshnaw) | [GitHub](https://github.com/gitrasheed)

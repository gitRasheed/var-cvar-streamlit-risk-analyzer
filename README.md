# 📊 VaR and CVaR Calculator: Financial Risk Analysis Tool

## Overview

This Streamlit web app calculates and visualizes Value at Risk (VaR) and Conditional Value at Risk (CVaR) for custom stock portfolios. I wanted to make this after first learning of CVaR from [this interview](https://youtu.be/pEkAICRqjvY?si=DpQ2xdIYrN4pu_tO) with Stanislav Uryasev.

## Features

### Portfolio Management

- Custom stock portfolio creation with flexible weightings
- Real-time market data via yfinance integration
- Adjustable portfolio value and time horizons

### Risk Calculation Methods

- Historical: Based on actual past returns
- Parametric: Normal distribution assumption
- Monte Carlo: Return distribution simulation

### Analysis Options

- Adjustable confidence levels (90% - 99%)
- Rolling window analysis for risk evolution
- Flexible date range selection

### Visualizations

- Return distribution histograms with VaR/CVaR markers
- Rolling window time series plots
- Monte Carlo simulation distributions

## Technical Stack

- Streamlit: Web framework
- Pandas & yfinance: Data handling
- SciPy: Statistical computations
- Plotly: Interactive visualizations
- Pytest: Testing framework

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run streamlit_app.py`

## Future Enhancements

- Historical crisis scenario stress testing
- Portfolio optimization using CVaR

## Acknowledgements

Inspiration for this project came from Prudhvi Reddy's implementation of a similar web application. Their work provided valuable insights into the practical application of financial risk metrics in a web environment.

[LinkedIn](https://www.linkedin.com/in/khoshnaw) | [GitHub](https://github.com/gitrasheed)

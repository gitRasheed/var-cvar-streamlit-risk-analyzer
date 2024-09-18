import numpy as np
from scipy import stats

def calculate_var_historical(returns, confidence_level):
    return abs(np.percentile(returns, 100 * (1 - confidence_level)))

def calculate_var_parametric(returns, confidence_level):
    mu = np.mean(returns)
    sigma = np.std(returns)
    return abs(stats.norm.ppf(1 - confidence_level, mu, sigma))

def calculate_var_monte_carlo(returns, confidence_level, num_simulations):
    mu = np.mean(returns)
    sigma = np.std(returns)
    simulated_returns = np.random.normal(mu, sigma, num_simulations)
    return abs(np.percentile(simulated_returns, 100 * (1 - confidence_level)))
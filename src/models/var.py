import numpy as np
from scipy import stats


def calculate_var_historical(returns, confidence_level, time_horizon):
    var_daily = abs(np.percentile(returns, 100 * (1 - confidence_level)))
    return var_daily * np.sqrt(time_horizon)


def calculate_var_parametric(returns, confidence_level, time_horizon):
    mu = np.mean(returns)
    sigma = np.std(returns)
    var_daily = abs(stats.norm.ppf(1 - confidence_level, mu, sigma))
    return var_daily * np.sqrt(time_horizon)


def calculate_var_monte_carlo(returns, confidence_level, time_horizon, num_simulations):
    mu = np.mean(returns)
    sigma = np.std(returns)
    simulated_returns = np.random.normal(
        mu, sigma * np.sqrt(time_horizon), num_simulations
    )
    var = abs(np.percentile(simulated_returns, 100 * (1 - confidence_level)))
    return var, simulated_returns

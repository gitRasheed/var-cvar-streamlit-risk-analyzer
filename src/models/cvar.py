import numpy as np
from scipy import stats
from src.models.var import calculate_var_historical, calculate_var_monte_carlo


def calculate_cvar_historical(returns, confidence_level, time_horizon):
    var = calculate_var_historical(returns, confidence_level, time_horizon)
    cvar_daily = abs(np.mean(returns[returns <= -var / np.sqrt(time_horizon)]))
    return cvar_daily * np.sqrt(time_horizon)


def calculate_cvar_parametric(returns, confidence_level, time_horizon):
    mu = np.mean(returns)
    sigma = np.std(returns)
    z_score = stats.norm.ppf(1 - confidence_level)
    cvar_daily = abs(mu + sigma * stats.norm.pdf(z_score) / (1 - confidence_level))
    return cvar_daily * np.sqrt(time_horizon)


def calculate_cvar_monte_carlo(
    returns, confidence_level, time_horizon, num_simulations
):
    var, simulated_returns = calculate_var_monte_carlo(
        returns, confidence_level, time_horizon, num_simulations
    )
    cvar = abs(np.mean(simulated_returns[simulated_returns <= -var]))
    return cvar, simulated_returns

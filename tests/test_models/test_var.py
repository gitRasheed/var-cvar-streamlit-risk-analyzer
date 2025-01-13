import pytest
import numpy as np
from src.models.var import (
    calculate_var_historical,
    calculate_var_parametric,
    calculate_var_monte_carlo,
)


@pytest.fixture
def sample_returns():
    return np.array([-0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04])


def test_calculate_var_historical(sample_returns):
    confidence_level = 0.95
    time_horizon = 1
    var = calculate_var_historical(sample_returns, confidence_level, time_horizon)
    assert isinstance(var, float)
    assert var >= 0
    assert var <= abs(min(sample_returns))


def test_var_time_horizon_scaling():
    returns = np.random.normal(0, 0.01, 1000)
    confidence_level = 0.95
    var_1day = calculate_var_historical(returns, confidence_level, 1)
    var_10day = calculate_var_historical(returns, confidence_level, 10)
    assert np.isclose(var_10day, var_1day * np.sqrt(10), rtol=1e-5)


def test_calculate_var_parametric(sample_returns):
    confidence_level = 0.95
    time_horizon = 1
    var = calculate_var_parametric(sample_returns, confidence_level, time_horizon)
    assert isinstance(var, float)
    assert var >= 0


def test_calculate_var_monte_carlo(sample_returns):
    confidence_level = 0.95
    time_horizon = 1
    num_simulations = 10000
    var = calculate_var_monte_carlo(
        sample_returns, confidence_level, time_horizon, num_simulations
    )
    assert isinstance(var, float)
    assert var >= 0

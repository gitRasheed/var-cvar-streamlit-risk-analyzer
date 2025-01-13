import pytest
import numpy as np
from src.models.cvar import (
    calculate_cvar_historical,
    calculate_cvar_parametric,
    calculate_cvar_monte_carlo,
)


@pytest.fixture
def sample_returns():
    return np.array([-0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04])


def test_calculate_cvar_historical(sample_returns):
    confidence_level = 0.95
    time_horizon = 1
    cvar = calculate_cvar_historical(sample_returns, confidence_level, time_horizon)
    assert isinstance(cvar, float)
    assert cvar >= 0
    assert cvar >= abs(min(sample_returns))


def test_cvar_time_horizon_scaling():
    returns = np.random.normal(0, 0.01, 1000)
    confidence_level = 0.95
    cvar_1day = calculate_cvar_historical(returns, confidence_level, 1)
    cvar_10day = calculate_cvar_historical(returns, confidence_level, 10)
    assert np.isclose(cvar_10day, cvar_1day * np.sqrt(10), rtol=1e-5)


def test_calculate_cvar_parametric(sample_returns):
    confidence_level = 0.95
    time_horizon = 1
    cvar = calculate_cvar_parametric(sample_returns, confidence_level, time_horizon)
    assert isinstance(cvar, float)
    assert cvar >= 0


def test_calculate_cvar_monte_carlo(sample_returns):
    confidence_level = 0.95
    time_horizon = 1
    num_simulations = 10000
    cvar = calculate_cvar_monte_carlo(
        sample_returns, confidence_level, time_horizon, num_simulations
    )
    assert isinstance(cvar, float)
    assert cvar >= 0

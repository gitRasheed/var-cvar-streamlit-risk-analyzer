import pytest
import numpy as np
from src.models.var import calculate_var_historical, calculate_var_parametric, calculate_var_monte_carlo

@pytest.fixture
def sample_returns():
    return np.array([-0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04])

def test_calculate_var_historical(sample_returns):
    confidence_level = 0.95
    var = calculate_var_historical(sample_returns, confidence_level)
    assert isinstance(var, float)
    assert var >= 0
    assert var <= abs(min(sample_returns))

def test_calculate_var_parametric(sample_returns):
    confidence_level = 0.95
    var = calculate_var_parametric(sample_returns, confidence_level)
    assert isinstance(var, float)
    assert var >= 0

def test_calculate_var_monte_carlo(sample_returns):
    confidence_level = 0.95
    num_simulations = 10000
    var = calculate_var_monte_carlo(sample_returns, confidence_level, num_simulations)
    assert isinstance(var, float)
    assert var >= 0
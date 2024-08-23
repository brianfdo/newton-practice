import pytest
import numpy as np
import math
import time

import newton

def test_basic_function():
    assert np.isclose(newton.newton_method(2.95, np.cos), 3.14, 0.03)

def test_numeric_input():
    with pytest.raises(TypeError):
        newton.newton_method(np.cos, 3, 1e-16)


def test_diverge():
    with pytest.raises(RuntimeError, match='Diverged'):
        newton.newton_method(2.95, np.cos, 1e-10)


def test_divide_0():
    with pytest.raises(ZeroDivisionError, match='float division by zero'):
        newton.newton_method(0, np.cos, 1e-10)


test_basic_function()
test_numeric_input()
test_divide_0()
test_diverge()
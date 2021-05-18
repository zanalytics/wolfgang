import pytest
from utils.stock_market import stock_market

def test_stock_market():
    data = stock_market("GOOG")
    data_shape = data.shape
    assert data_shape[0] >= 30 and data_shape[1] == 7
import pytest
from price_calculator import PriceCalculator

@pytest.mark.parametrize("subtotal, expected", [
    (100, 121.00),
    (0, 0.00),
    (554, 670.34),
    (222, 268.62),
    (37, 44.77)
])
def test_apply_iva(subtotal, expected):
    assert PriceCalculator.apply_iva(subtotal) == expected
    

@pytest.mark.parametrize("subtotal, percent, expected", [
    (100, 10, 90),
    (0, 0, 0.00),
    (333, 50, 166.5),
    (888, 100, 0.00),
    (100, 33, 67.00),
    (53, 33, 35.51)
])
def test_apply_discount(subtotal, percent, expected):
    assert PriceCalculator.apply_discount(subtotal, percent) == expected


@pytest.mark.parametrize("percent", [-1, 101, 150])
def test_invalid_percent_raises(percent):
    with pytest.raises(ValueError):
        PriceCalculator.apply_discount(100, percent)
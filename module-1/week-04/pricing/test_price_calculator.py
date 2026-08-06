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
    with pytest.raises(ValueError, match="Percent must be between 0 and 100."):
        PriceCalculator.apply_discount(100, percent)

@pytest.mark.parametrize("subtotal, coupon, expected", [
    (100, 50, 50),
    (100, 100, 0),
    (1523, 800, 723),
    (8888, 8, 8880)
])
def test_apply_coupon(subtotal, coupon, expected):
    assert PriceCalculator.apply_coupon(subtotal, coupon) == expected

@pytest.mark.parametrize("coupon", [200, 300, 856])
def test_invalid_coupon_raises(coupon):
    with pytest.raises(ValueError, match="The coupon amount cannot exceed the subtotal."):
        PriceCalculator.apply_coupon(100, coupon)

@pytest.mark.parametrize("subtotal, cost, threshold, expected", [
    (100, 50, 120, 150),
    (100, 50, 90, 100),
    (600, 50, 500, 600),
    (500, 50, 500, 500)

])
def test_apply_shipping(subtotal, cost, threshold, expected):
    assert PriceCalculator.apply_shipping(subtotal, cost, threshold) == expected

@pytest.mark.parametrize("cost", [-2, -300, -999])
def test_invalid_cost_raises(cost):
    with pytest.raises(ValueError, match="Cost must be greater than 0."):
        PriceCalculator.apply_shipping(100, cost)
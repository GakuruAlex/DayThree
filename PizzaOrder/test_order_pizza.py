import pytest
from order_pizza import order_pizza

# test order pizza function  Y is yes, N no, L large, S small, M medium
@pytest.mark.parametrize("size, pepperoni, cheese, bill", [
    ('S','Y','Y', 18),
    ('M','N','Y', 21),
    ('L','Y','Y', 29)
])
class TestOrderPizza:
    def test_order_pizza(self, size, pepperoni, cheese, bill):
        assert order_pizza(size, pepperoni, cheese) == bill
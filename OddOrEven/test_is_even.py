import pytest

from is_even import is_even

@pytest.mark.parametrize("number, result",[
    (2, True),
    (3, False),
    (100, True),
    (299, False),
    (-25, False),
    (-44, True),
    (-30, True)
])

class TestIsEven:
    def test_is_even(self, number, result):
        assert is_even(number) == result
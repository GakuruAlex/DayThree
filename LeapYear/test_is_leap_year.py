import pytest
from is_leap_year import is_leap_year

# Test divisible by 4 and not 100 or 400
@pytest.mark.parametrize("year, is_leap",[
    (1904, True),
    (1992, True),
    (1996, True),
    (2148, True),
    (2196, True),
   
])
class TestIsLeapYearWithFour:
    def test_is_leap_year_by_four(self, year, is_leap):
        assert is_leap_year(year) == is_leap


# Test is leap for divisible by 4 and 100 but not 400
@pytest.mark.parametrize("year, is_leap",[
    (1900, False),
    (2100, False),
    (2200, False),
    (2300, False),
    (2500, False),
    (2700, False),
])

class TestIsLeapYearWithFourHundred:
    def test_is_leap_year_for_divisible_by_4_100_but_not_400(self, year, is_leap):
        assert is_leap_year(year) == is_leap

#Test is leap year for divisible by 4, 100 and 400
@pytest.mark.parametrize("year, is_leap",[
    (2400, True),
    (2800, True),
    (3200, True)
])

class TestIsLeapYearWith100And100:
    def test_is_leap_year_for_divisible_by_4_100_and_400(self, year, is_leap):
        assert is_leap_year(year) == is_leap


# Test years not leap 
@pytest.mark.parametrize("year, is_leap",[
    (1949, False),
    (2229, False),
    (1999, False),
    (2341, False),
    (2023, False)
])

class TestIsLeapFailures:
    def test_is_leap_year_for_years_not_leap(self, year, is_leap):
        assert is_leap_year(year) == is_leap


@pytest.mark.xfail(reason="This test is meant to fail")
def test_is_leap_year_failure(self):
    assert is_leap_year(2021) == True
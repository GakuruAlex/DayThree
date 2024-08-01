import pytest
from bmi_calculator_2 import bmi_calculator,categorize_bmi

#Test bmi calculator
@pytest.mark.parametrize("weight, height, bmi",[
    (85, 1.8, 26.23),
    (90, 1.6, 35.16),
    (8, 2, 2),
    (72, 1.65, 26.45)
])
class TestBMICalculator:
    def test_bmi_calculator_2(self, weight, height, bmi):
        assert bmi_calculator(weight, height) == bmi


#Test BMI categorization
@pytest.mark.parametrize("bmi, category",[
    (26, 'slightly overweight'),
    (18, 'underweight'),
    (20, 'normal weight'),
    (33, 'obese'),
    (35, 'clinically obese'),
    (40, 'clinically obese'),
    (12, 'underweight'),
    (18.5, 'normal weight'),
    (25, 'slightly overweight'),
    (30, 'obese')
])
class TestCategorizeBMI:
    def test_categorize_bmi(self, bmi, category):
        assert categorize_bmi(bmi) == category
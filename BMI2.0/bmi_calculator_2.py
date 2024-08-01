def bmi_calculator(weight: float, height: float) -> float:
    """_Calculate bmi given height and weight_

    Args:
        weight (float): _given weight_
        height (float): _given height_

    Returns:
        float: _bmi_
    """
    return  round(weight / (height * height), 2) #Round to two decimal places

def categorize_bmi(bmi: float) -> str:
    """_Categorize given bmi_

    Args:
        bmi (float): _bmi_

    Returns:
        str: __Category bmi falls under
    """
    if bmi < 18.5:
        return f"underweight"
    elif bmi >= 18.5 and bmi < 25:
        return f"normal weight"
    elif bmi >= 25 and bmi < 30:
        return f"slightly overweight"
    elif bmi >= 30 and bmi < 35:
        return f"obese"
    elif bmi >= 35:
        return f"clinically obese"
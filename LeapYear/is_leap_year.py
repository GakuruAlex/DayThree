def is_leap_year(year: int) -> bool:
    """_Function checks whether a given year is leap_

    Args:
        year (int): _Year to check_

    Returns:
        bool: _True if leap else False_
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
                return False
        else:
            return True
    else:
        return False

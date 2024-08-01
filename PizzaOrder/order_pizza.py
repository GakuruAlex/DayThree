def order_pizza(size: str, pepperoni: str, cheese: str)-> float:
    """_Function to calculate the total bill for a pizza order_

    Args:
        size (str): _Size of the pizza_
        pepperoni (str): _Whether to add pepperoni_
        cheese (str): _Whether to add cheese_

    Returns:
        float: _Total bill_
    """
    total: float = 0.0

    if size == "S":
        total += 15
        if pepperoni == "Y":
            total += 2
    elif size == "M":
        total += 20
        if pepperoni == "Y":
            total +=  2

    else:
        total += 25
        if pepperoni == "Y":
            total += 3
    if cheese == "Y":
        total += 1
    return total

def cross_road_move(move: str)-> bool:
    """_Choose which direction to take_

    Args:
        move (str): _chosen direction_

    Returns:
        bool: _True if left otherwise False_
    """
    return True if move.lower() == "left" else False

def river_move(move: str)-> bool:
    """_Section to choose which direction at a river_

    Args:
        move (str): _User move_

    Returns:
        bool: _True if wait else False_
    """
    return True if move.lower() == "wait" else False

def which_door(door: str)-> str:
    """_Choosing which door_

    Args:
        door (str): _door chosen by user among blue, red, yellow_

    Returns:
        str: _Output whether game is won or over_
    """
    if door.lower() == "red":
        return 'Wrong door!You fell into a volcano. Game Over!'
    elif door.lower() == "blue":
        return 'Ooops! You teleported into a black hole. Gave Over.'
    elif door.lower() == "yellow":
        return 'You won!'
    else:
        return 'Game Over!'
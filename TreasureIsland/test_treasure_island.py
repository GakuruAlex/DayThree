import pytest

from treasure_island import cross_road_move, river_move, which_door

@pytest.mark.parametrize("move, is_alive", [
    ('left', True),
    ('right', False),
    ('hey', False),
    ('1', False),
    ('Right', False),
    ('RIGHT', False),
    ('LEFT', True),
    ('Left', True),
    ('LeFT', True)
])

class TestCrossRoadMove:
    def test_cross_road_move(self, move, is_alive):
        assert cross_road_move(move) == is_alive

@pytest.mark.parametrize("move, is_alive",[
    ('left', False),
    ('wait', True),
    ('WAIT', True),
    ('Wait', True),
    ('right', False),
    ('down', False)
])

class TestRiverMove:
    def test_river_move(self, move, is_alive):
        assert river_move(move) == is_alive

@pytest.mark.parametrize("move, message",[
    ('red', 'Wrong door!You fell into a volcano. Game Over!'),
    ('blue','Ooops! You teleported into a black hole. Gave Over.'),
    ('yellow', 'You won!'),
    ('anything else', 'Game Over!'),
    ('back', 'Game Over!')
])
class TestWhichDoor:
    def test_which_door(self, move, message):
        assert which_door(move) == message
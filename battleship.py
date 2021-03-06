import enum
import random
import numpy as np


def get_random_tuple():
    """
    This method generates a 2-tuple containing values between 0 and 9.
    :return: 2-tuple of ints
    """
    return np.random.randint(0, 10), np.random.randint(0, 10)


def get_random_direction():
    """
    This method randomly generates a direction (vertical or horizontal)
    :return: "horizontal" or "vertical"
    """
    # TODO(8): Create the logic for this method based on the docstring above.


def point_out_of_bounds(tuplevalue):
    """
    This method checks to make sure the tuple is a valid point on the 10x10 battleship board
    :param tuplevalue: 
    :return: 
    """
    # TODO(7): Create the logic for this method based on the docstring above.

def point_valid(ship_list, tuplevalue):
    """
    This method checks to see if tuplevalue is a valid move on the board. (aka, cannot be the spot of a current ship, 
    or partially off the board) :param ship_list: :param tuplevalue: :return: 
    """
    # TODO(6): Create the logic for this method based on the docstring above.


def create_ship(length, ship_list):
    """
    This method randomly picks a direct, and starting location for a ship. It generates a list of parameter length 
    coordinates(2-tuples). The list must be a valid ship and of the provided length.
    :param length: 
    :param ship_list: :return: 
    """
    # TODO(2): Create the logic for this method based on the docstring above.

def get_random_ship_positions():
    """
    This method generates 5 ships and adds each ship to a list. Use the create_ship method. 
    :return: 
    """
    # TODO(4): Create the logic for this method based on the docstring above


class GameState(enum.Enum):
    SETUP = "Setup"
    MIDGAME = "Midgame"


class Opponent:
    def __init__(self):
        self.ships = get_random_ship_positions()
        self.shots = []

    def take_turn(self):
        """
        This recursive method randomly selects a point. If the point has not been fired at, add it to the list of points
        that have been fired at. If the point has been fired at previously, enter a recursive loop until an available 
        coordinate can be fired at.
        :return: the 2 tuple representing the coordinate fired at
        """
        # TODO(8): Create the logic for this method based on the docstring above.


class Battleship:
    def __init__(self):
        self.game_state = GameState.SETUP
        self.opponent = Opponent()
        self.opponent_ships = self.opponent.ships
        self.player_ships = []
        self.turn = 1

    def player_fire(self, x, y):
        """
        This method checks if the (x, y) coordinate is a position on a ship, if it is, return "hit" otherwise "miss". 
        When a ship is hit, remove the coordinate from self.opponent_ships. When the list is empty, print "You win! 
        and close the program. :param x: :param y: :return: 
        """
        for ship in self.opponent_ships:
            if (x, y) in ship:
                ship.remove((x, y))
                if (len(ship) == 0):
                    self.opponent_ships.remove(ship)
                    if (len(self.opponent_ships) == 0):
                        print("You win!")
                        exit()
                return "hit"
        return "miss"

    def opponent_fire(self):
        """
        This method calls on the opponent to take a turn and then check if it was a hit or a miss. If it was a hit, 
        return a tuple in the form of (<result>, x, y), where <result> is the shot was a hit/miss, and x/y is the coordinate return from
        self.opponent.take_turn()
        When a ship is hit, remove the coordinate from self.player_ships. When the list is empty, print "You lose! 
        :return: a tuple containing 
        """
        #TODO(1): Create the logic for this method based on the docstring above.

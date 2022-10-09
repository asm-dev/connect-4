from settings import BOARD_LENGHT, VICTORY_STRIKE
from list_utils import find_streak

class LinearBoard():
    """
    This class represents a 1-column board. Two characters are used as game pieces, e.g. 'x' for player A, 'o' for player B.
    None represents an empty space 
    """

    def __init__(self):
        """
        We initiate our board empty/full of None, as many None as set by BOARD_LENGHT
        """
        self._column = [None for i in range(BOARD_LENGHT)] # same as [None] * BOARD_LENGHT  

    def add(self, char):
        """
        Adds a new game piece to the column, using the first available space. We use characters as game pieces
        """
        # As long as the board isn't full
        if not self.is_full():
            # Find the closest None
            idx = self._column.index(None)
            # Swap it for the appropiate game piece/character
            self._column[idx] = char

    def is_full(self):
        """
        Returns true when the board is full
        """
        # As long as the last element is None, then the board isn't full yet
        if self._column[-1] == None:
            return False
        else:
            return True  

    def is_victory(self, char):
        return find_streak(self._column, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        """
        If the board is full and no one has won, then it's a tie
        """
        if (self.is_victory(char1) == False) and (self.is_victory(char2) == False) and self.is_full():
            return True
        else:
            return False
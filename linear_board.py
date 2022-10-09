from settings import BOARD_LENGHT, VICTORY_STRIKE
from list_functions import find_streak

class LinearBoard():
    def __init__(self):
        """
        We initiate our board empty/full of None
        """
        self.column = [None] * BOARD_LENGHT

    def is_full(self):
        """
        This returns true when the board is full
        """
        # As long as the last element is None, then the board isn't full yet
        if self.column[-1] == None:
            return False
        else:
            return True     

    def add(self, piece):
        """
        Adds a new game piece to the relevant column, using the first available space
        """
        # As long as the board isn't full
        if not self.is_full():
            # Find the closest None
            idx = self.column.index(None)
            # Swap it for the appropiate game piece
            self.column[idx] = piece

    def is_victory(self, char):
        return find_streak(self.column,char, VICTORY_STRIKE)

    def is_tie(self, piece1, piece2):
        # si no hay victoria de nadie, pues hay empate
        if (self.is_victory(piece1) == False) and (self.is_victory(piece2) == False) and self.is_full():
            return True
        else:
            return False
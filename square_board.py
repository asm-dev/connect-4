from linear_board import LinearBoard
from settings import BOARD_LENGHT


class SquareBoard:
    """
    This class represents a square board. It combines 4 columns (4 LinearBoards)
    """

    def __init__(self):
        self._columns = [LinearBoard() for i in range (BOARD_LENGHT)] 
    
    def add(self, char, index):
        pass

    def is_full(self):
        """
        Returns True if all LinearBoards are full
        """
        all_full = True
        for lboard in self._columns:
            all_full = all_full and lboard.is_full()
        return all_full

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    def _any_vertical_victory(self, char):
        victory = False
        for lboard in self._columns:
            victory = victory or lboard.is_victory(char)
        return victory

    def _any_horizontal_victory(self, char):
        return False

    def _any_rising_victory(self, char):
        return False

    def _any_sinking_victory(self, char):
        return False

    # dunders
    def __repr__(self):
        return f"{self.__class__}:{self._columns}"
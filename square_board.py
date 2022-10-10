from linear_board import LinearBoard
from settings import BOARD_LENGHT


class SquareBoard:
    """
    This class represents a square board. It combines X columns (X LinearBoards), depending on BOARD_LENGHT settings
    """

    @classmethod
    def fromList(cls, list_of_lists):
        """
        It tansforms a lists of lists (list of ) into a list of LinearBoard
        """
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board


    def __init__(self):
        self._columns = [LinearBoard() for i in range (BOARD_LENGHT)] 
    
    def add(self, char, index):
        self._columns[index].add(char)
        pass

    def as_matrix(self):
        """
        Returns its representation as a matrix
        """
        matrix = []
        for linear_board in self._columns:
            matrix.append(linear_board.as_list())
        return matrix

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
        # return reduce(self._columns, False, lambda x, y : x.is_victory() or y.is_victory())
        victory = False
        for lboard in self._columns:
            victory = victory or lboard.is_victory(char)
        return victory

    def _any_horizontal_victory(self, char):
        # a horizontal victory is a transposed vertical victory
        return False

    def _any_rising_victory(self, char):
        return False

    def _any_sinking_victory(self, char):
        return False

    # dunders
    def __repr__(self):
        return f"{self.__class__}:{self._columns}"
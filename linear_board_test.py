import pytest
from linear_board import *
from settings import BOARD_LENGHT, VICTORY_STRIKE

def test_empty_board():
    empty = LinearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False

def test_add():
    board = LinearBoard()
    for i in range(BOARD_LENGHT):
        board.add('x')
    assert board.is_full()

def test_victory():
    board = LinearBoard()
    for i in range(VICTORY_STRIKE):
        board.add('x')
    assert board.is_victory('o') == False
    assert board.is_victory('x')

def test_tie():
    board = LinearBoard()
    board.add('o')
    board.add('o')
    board.add('x')
    board.add('o')
    assert board.is_tie('x', 'o')
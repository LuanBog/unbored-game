import sys

sys.path.insert(1, './games')

from hangman import Hangman
from rps import Rps 
from tictactoe import Tictactoe

def load():
    return [Hangman, Rps, Tictactoe]

import sys

sys.path.insert(1, './games')

from hangman import Hangman
from rps import Rps 
from tictactoe import Tictactoe
from guess_the_number import Guess_the_number

def load():
    return [Hangman, Rps, Tictactoe, Guess_the_number]

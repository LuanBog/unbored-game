import sys

sys.path.insert(1, './games')

from hangman import Hangman
from rps import Rps 

def load():
    return [Hangman, Rps]

import random

class Game:
    title = 'Game'
    won = False



class Hangman(Game):
    title = 'Hangman'

    hangman_pictures = ['''

        +---+
        |   |
        |   |
            |
            |
            |
    ===========''','''

        +---+
        |   |
        |   |
        o   |
            |
            |
    ===========''','''

        +---+
        |   |
        |   |
        o   |
        |   |
            |
    ===========''','''

        +---+
        |   |
        |   |
        o   |
       /|   |
            |
    ===========''','''

        +---+
        |   |
        |   |
        o   |
       /|\  |
            |
    ===========''','''

        +---+
        |   |
        |   |
        o   |
       /|\  |
       /    |
    ===========''','''

        +---+
        |   |
        |   |
        o   |
       /|\  |
       / \  |
    ===========''']

    words = ['red', 'black', 'furniture', 'apple', 'kingdom', 'prince', 'milk', 'chair', 'doctor', 'minecraft', 'terraria', 'utility', 'kick', 'mouse', 'joke', 'dumb', 'cool', 'pro', 'roblox', 'fabric', 'discord', 'coco', 'castle', 'movie', 'howl', 'hat']

    def __init__(self):
        self.word_chosen = random.choice(Hangman.words)
        self.tries = 0
        self.guess_result = '_ ' * len(self.word_chosen)
        self.guess_result = self.guess_result.strip()

    def display_progress(self):
        print(Hangman.hangman_pictures[self.tries])
        print('')
        print('Tries: {}/{}'.format(self.tries, len(Hangman.hangman_pictures) - 1))
        print('')
        print(self.guess_result)
        print('')

    def change_letter(self, word, letter, position):
        word = word.strip().split()

        result = ''

        for index, lett in enumerate(word):
            if lett == '_':
                if index == position:
                    result = result + letter + ' '
                else:
                    result = result + '_ '
            else:
                result = result + lett + ' '

        return result.strip()

    def run(self):
        while True:
            self.display_progress()

            if self.tries == len(Hangman.hangman_pictures) - 1:
                print('You lost! You let the man die. The word was \"{}\"'.format(self.word_chosen))
                Game.won = False
                break

            if not '_' in self.guess_result:
                Game.won = True
                break

            letter_input = input('Letter that you think that\'s in the word: ').lower()

            if letter_input in self.word_chosen:
                for index, letter in enumerate(self.word_chosen):
                    if letter == letter_input:
                        self.guess_result = self.change_letter(self.guess_result, letter_input, index)
            else:
                print('It\'s not in there!')
                self.tries += 1



class Rps(Game):
    title = 'Rock Paper Scissors'

    def result(self, player, opposition):
        if (player == 'r' and opposition == 's') or (player == 's' and opposition == 'p') or (player == 'p' and opposition == 'r'):
            return 'player'
        elif (opposition == 'r' and player == 's') or (opposition == 's' and player == 'p') or (opposition == 'p' and player == 'r'):
            return 'opposition'
        else:
            return 'tie'

    def prettify(self, arg):
        if arg == 'r':
            return 'rock'
        elif arg == 'p':
            return 'paper'
        else:
            return 'scissors'

    def run(self):
        while True:
            opposition_input = random.choice(['r', 'p', 's'])
            player_input = input('[r]ock [p]aper [s]cissors?: ').lower()

            result = self.result(player_input, opposition_input)

            if result == 'player':
                print('{} beats {}, congrats!'.format(self.prettify(player_input), self.prettify(opposition_input)))
                Game.won = True
                break
            elif result == 'opposition':
                print('{} can\'t beat {}, congrats!'.format(self.prettify(player_input), self.prettify(opposition_input)))
                Game.won = False
                break
            else:
                print('{} can\'t beat itself. It\'s a tie, try again!'.format(self.prettify(player_input)))

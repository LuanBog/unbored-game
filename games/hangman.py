from game import Game
import random

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
        super().__init__()
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
        while self.running:
            self.display_progress()

            if self.tries == len(Hangman.hangman_pictures) - 1:
                print('You lost! You let the man die. The word was \"{}\"'.format(self.word_chosen))
                self.lose()
                break

            if not '_' in self.guess_result:
                print('You won! You set the man free.')
                self.win()
                break

            letter_input = input('Letter that you think that\'s in the word: ').lower()

            if letter_input in self.word_chosen:
                for index, letter in enumerate(self.word_chosen):
                    if letter == letter_input:
                        self.guess_result = self.change_letter(self.guess_result, letter_input, index)
            else:
                print('It\'s not in there!')
                self.tries += 1

if __name__ == '__main__':
    game = Hangman()
    game.run()

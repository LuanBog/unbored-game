from game import Game
import sys
import random
import json
import colorama
from colorama import Fore

colorama.init(autoreset=True)

sys.path.insert(1, '../')
from form import Form

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

    def __init__(self, player):
        super().__init__(player)
        self.word_chosen = ''
        self.guess_result = ''
        self.category = None
        self.tries = 0

    def display_progress(self):
        print(Hangman.hangman_pictures[self.tries])
        print('')
        print(f'Category: {Fore.YELLOW}{self.category}')
        print(f'Tries: {Fore.GREEN}{self.tries}{Fore.WHITE}/{Fore.RED}{len(Hangman.hangman_pictures) - 1}')
        print('')
        print(self.guess_result)
        print('')

    def change_letter(self, word, letter, position):
        # Possible refactor
        def custom_split(word):
            result = []
            words = []

            word = word.split('  ')

            for element in word:
                words.append(element.split())

            for element in words:
                element.insert(len(element), ' ')

            for i in words:
                for v in i:
                    result.append(v)

            if result[-1] == ' ':
                del result[-1]

            return result

        word = custom_split(word.strip())

        result = ''

        for index, lett in enumerate(word):
            if lett == '_':
                if index == position:
                    result = result + letter + ' '
                else:
                    result = result + '_ '
            elif lett == ' ':
                result = result + ' '
            else:
                result = result + lett + ' '

        return result.strip()

    def ask_category(self):
        data = None

        file = './others/hangman_words.json' if __name__ == '__main__' else './games/others/hangman_words.json'
        with open(file) as f:
            data = json.load(f)

        choices = [category.title() for category in list(data.keys())]
        choices.append('Random')

        categories_menu = Form('Categories', choices)
        categories_menu_input = categories_menu.ask()

        category_chosen = None

        # Possible refactor
        if categories_menu_input['choice'] == 'Random':
            random_choice = random.choice(list(data.keys()))
            
            for category in list(data.keys()):
                if random_choice == category:
                    category_chosen = data[category]
                    break
        else:
            for category in list(data.keys()):
                if categories_menu_input['choice'].lower() == category:
                    category_chosen = data[category]
                    break

        self.category = categories_menu_input['choice']
        self.word_chosen = random.choice(category_chosen)

        for letter in self.word_chosen:
            if letter != ' ':
                self.guess_result = self.guess_result + '_ '
            else:
                self.guess_result = self.guess_result + ' '

    def run(self):
        while self.running:
            # Asks for category
            while not self.word_chosen:
                self.ask_category()

            self.display_progress()

            if self.tries == len(Hangman.hangman_pictures) - 1:
                print(f'{Fore.RED}You lost! You let the man die. The word was {Fore.YELLOW}\"{self.word_chosen}\"')
                self.lose()
                break

            if not '_' in self.guess_result:
                print(f'{Fore.GREEN}You won! You set the man free.')
                self.win()
                break

            letter_input = input('Letter that you think that\'s in the word: ').lower()

            if letter_input in self.word_chosen:
                for index, letter in enumerate(self.word_chosen):
                    if letter == letter_input:
                        self.guess_result = self.change_letter(self.guess_result, letter_input, index)
            else:
                print(f'{Fore.RED}It\'s not in there!')
                self.tries += 1

if __name__ == '__main__':
    game = Hangman(None)
    game.run()

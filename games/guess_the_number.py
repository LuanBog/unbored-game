from game import Game
import random
import colorama
import time
from colorama import Fore

colorama.init(autoreset=True)

class Guess_the_number(Game):
    title = 'Guess the number'

    def __init__(self, player):
        super().__init__(player)
        self.tries = 0
        self.max_tries = 10
        self.min = 1
        self.max = 100

        self.chosen_number = random.randrange(self.min, self.max + 1)

    def run(self):
        while self.running:
            print(f'\nTries: {Fore.GREEN}{self.tries}{Fore.WHITE}/{Fore.RED}{self.max_tries}')

            try:
                player_guess = int(input('Guess the number between {}-{}: '.format(self.min, self.max)))
            except ValueError:
                print(f'\n{Fore.RED}Invalid input. Please try again!')
                time.sleep(0.5)
                continue

            if self.tries >= self.max_tries:
                print(f'{Fore.RED}Better luck next time! {Fore.YELLOW}{self.chosen_number} {Fore.WHITE}is the number')
                self.lose()
                break

            if player_guess > self.chosen_number:
                print(f'Go {Fore.BLUE}lower!')
                self.tries += 1
            elif player_guess < self.chosen_number:
                print(f'Go {Fore.YELLOW}higher!')
                self.tries += 1
            elif player_guess == self.chosen_number:
                print(f'\n{Fore.GREEN}You guessed it! {Fore.YELLOW}{self.chosen_number} {Fore.WHITE}is the number')
                self.win()
                break

if __name__ == '__main__':
    game = Guess_the_number(None)
    game.run()

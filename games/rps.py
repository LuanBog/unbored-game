from game import Game
import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)

class Rps(Game):
    title = 'Rock Paper Scissors'

    def __init__(self, player):
        super().__init__(player)

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
        while self.running:
            opposition_input = random.choice(['r', 'p', 's'])
            player_input = input('[r]ock [p]aper [s]cissors?: ').lower()

            if player_input != 'r' and player_input != 'p' and player_input != 's':
                print(f'{Fore.RED}\nThat is invalid input!\n')
                continue

            result = self.result(player_input, opposition_input)

            print('')
            if result == 'player':
                print(f'{Fore.BLUE}{self.prettify(player_input)} {Fore.WHITE}beats {Fore.RED}{self.prettify(opposition_input)}{Fore.WHITE}, {Fore.GREEN}congrats you won!')
                self.win()
                break
            elif result == 'opposition':
                print(f'{Fore.BLUE}{self.prettify(player_input)} {Fore.WHITE}can\'t beat {Fore.RED}{self.prettify(opposition_input)}{Fore.WHITE}, {Fore.RED}you lost!')
                self.lose()
                break
            else:
                print(f'{Fore.BLUE}{self.prettify(player_input)} {Fore.WHITE}can\'t beat itself. It\'s a tie, try again!'.format(self.prettify(player_input)))
            print('')
            
if __name__ == '__main__':
    game = Rps(None)
    game.run()
    
from game import Game
import random

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

            if player_input != 'r' and player_input != 'p' and player_input != 's':
                print('\nThat is invalid input!\n')
                continue

            result = self.result(player_input, opposition_input)

            print('')
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
            print('')
            
if __name__ == '__main__':
    game = Rps()
    game.run()
    
from game import Game
import time
import sys
import random

sys.path.insert(1, './games')

from form import Form

class Tictactoe(Game):
    # X = Player playing. O = Opposite player or Bot

    title = 'Tic-Tac-Toe'

    def __init__(self, player, players):
        super().__init__(player)

        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']
        self.turn = {
            'player': player,
            'letter': 'X'
        }
        self.players = players
        self.opposing_player = None
        self.against_bot = False

    def display_board(self, show_index = False):
        if show_index:
            print('{} | {} | {}'.format(self.board[0] if self.board[0] != ' ' else '1', self.board[1] if self.board[1] != ' ' else '2', self.board[2] if self.board[2] != ' ' else '3'))
            print('--+---+--')
            print('{} | {} | {}'.format(self.board[3] if self.board[3] != ' ' else '4', self.board[4] if self.board[4] != ' ' else '5', self.board[5] if self.board[5] != ' ' else '6'))
            print('--+---+--')
            print('{} | {} | {}'.format(self.board[6] if self.board[6] != ' ' else '7', self.board[7] if self.board[7] != ' ' else '8', self.board[8] if self.board[8] != ' ' else '9'))
        else:
            print('{} | {} | {}'.format(self.board[0], self.board[1], self.board[2]))
            print('--+---+--')
            print('{} | {} | {}'.format(self.board[3], self.board[4], self.board[5]))
            print('--+---+--')
            print('{} | {} | {}'.format(self.board[6], self.board[7], self.board[8]))

    def insert(self, cell, letter):
        if self.board[cell] == ' ':
            self.board[cell] = letter

    def is_winner(self, letter, custom_board = None):
        board = custom_board if custom_board else self.board

        return (board[0] == letter and board[1] == letter and board[2] == letter) or (board[3] == letter and board[4] == letter and board[5] == letter) or (board[6] == letter and board[7] == letter and board[8] == letter) or (board[0] == letter and board[3] == letter and board[6] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter)

    def find_best_cell(self):
        # Credits: Tech with tim

        possible_cells = [index for index, letter in enumerate(self.board) if letter == ' ']

        # Checks for winning cells or cells to block
        for letter in ['O', 'X']:
            for index in possible_cells:
                board_copy = self.board.copy()
                board_copy[index] = letter

                if self.is_winner(letter, board_copy):
                    return index

        # Corners
        corners = []
        for index in possible_cells:
            if index in [0, 2, 6, 8]:
                corners.append(index)
        if len(corners) > 0:
            return random.choice(corners)

        # Center
        if 4 in possible_cells:
            return 4

        # Edges
        edges = []
        for index in possible_cells:
            if index in [1, 5, 7, 3]:
                edges.append(index)
        if len(edges) > 0:
            return random.choice(index)

        return None

    def run(self):
        selected = False

        while self.running:
            while not selected:
                selection = input('Play against [bot / player]: ').lower()

                if selection == 'player':
                    choices = []

                    for player in self.players:
                        if player.name == 'Guest' or player.name == self.player.name:
                            continue

                    choices.append(player.name)

                    opposing_player_menu = Form('Choose opposing player', choices)
                    opposing_player_menu_input = opposing_player_menu.ask()

                    for player in self.players:
                        if player.name == opposing_player_menu_input['choice']:
                            self.opposing_player = player

                    print('\nPlaying against {}\n'.format(self.opposing_player.name))

                    selected = True
                else:
                    print('\nPlaying against a bot\n')

                    self.against_bot = True
                    selected = True

            self.display_board(show_index=True)

            cell = None

            if self.against_bot and self.turn['letter'] == 'O':
                print('\nBot is making a move...\n')
                cell = self.find_best_cell()
            else:
                print('\n{} ({})\'s turn'.format(self.turn['player'].name, self.turn['letter']))
                cell = int(input('Which cell do you want to choose: ')) - 1

            if cell < 0 or cell > len(self.board):
                print('\nThat is not a cell!\n')
                time.sleep(1)
                continue

            if self.board[cell] != ' ':
                print('\nThat cell is already taken. Pick another!\n')
                time.sleep(1)
                continue

            self.insert(cell, self.turn['letter'])
            is_winner = self.is_winner(self.turn['letter'])

            if is_winner and self.turn['letter'] == 'X':
                self.display_board()
                print('\n{} (X) won! {} (O) lost...'.format(self.player.name, self.opposing_player.name if self.opposing_player else 'Bot'))
                
                if self.opposing_player:
                    self.opposing_player.score['loses'] += 1

                self.win()
                break
            elif is_winner and self.turn['letter'] == 'O':
                self.display_board()
                print('\n{} (O) won! {} (X) lost...'.format(self.opposing_player.name if self.opposing_player else 'Bot', self.player.name))
                
                if self.opposing_player:
                    self.opposing_player.score['wins'] += 1

                self.lose()
                break
            elif not is_winner and ' ' not in self.board:
                self.display_board()
                print('\nIt\'s a tie!')
                self.running = False
                break

            # Switch
            if self.turn['letter'] == 'X':
                if self.opposing_player:
                    self.turn = {
                        'player': self.opposing_player,
                        'letter': 'O'
                    }
                else:
                    self.turn = {
                        'player': None,
                        'letter': 'O'
                    }

            else:
                self.turn = {
                    'player': self.player,
                    'letter': 'X'
                }

if __name__ == '__main__':
    game = Tictactoe(None)
    game.run()

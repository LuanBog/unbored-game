class Game:
    title = 'Game'

    def __init__(self, player = None):
        self.running = True
        self.won = False

        if player:
            self.player = player
        else:
            self.player = None

    def win(self):
        if self.player:
            self.player.score['wins'] += 1

        self.running = False
        self.won = True

    def lose(self):
        if self.player:
            self.player.score['loses'] += 1

        self.running = False
        self.won = False

    # Purpose: Should always start with "while self.running:". If the player wins, call self.win() and self.lose() if they lose, followed with break
    def run(self):
        # while self.running:
        #     if 1 == 1:
        #         self.win()
        pass

##### EXAMPLE #####
class Example_Game(Game):
    def __init__(self, player):
        super().__init__(player)

    def run(self):
        while self.running:
            answer = input('Would you like to win? (y/n): ').lower()

            if answer == 'y' or answer == 'yes':
                self.win()
                break
            else:
                self.lose()
                break

if __name__ == '__main__':
    game = Example_Game(None)
    game.run()
